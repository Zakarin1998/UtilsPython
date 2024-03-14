# core.py
from DB.dati_utente import DBDatiUtente
from business.enrichment import Enricher
from business.validation import Validator
from input.input import InputUser


class Core:
    def __init__(self):
        self.db_utenti = DBDatiUtente()
        self.enricher = Enricher()
        self.validator = Validator()

    def execute(self):
        print("Benvenuto!")
        running = True
        while running:
            try:
                operazione = input("Cosa vuoi fare? (Inserimento/Ricerca/Visualizza/Cancellazione/Modifica/Exit): ").upper()

                if operazione == "INSERIMENTO":
                    utente = self.inserisci_dati()
                    self.validazione(utente)
                    self.arricchisci(utente, self.calcola_num_utenti())
                    self.inserisci_db(utente)
                    print("Utente inserito:", utente)

                elif operazione == "RICERCA":
                    user_id_ric = self.inserisci_id()
                    self.ricerca_per_id(user_id_ric)

                elif operazione == "VISUALIZZA":
                    self.visualizza_tutti()

                elif operazione == "CANCELLAZIONE":
                    user_id_canc = self.inserisci_id()
                    self.cancella_per_id(user_id_canc)

                elif operazione == "MODIFICA":
                    user_id_upd = self.inserisci_id()
                    utente_toup = self.db_utenti.find_by_id(user_id_upd)

                    if utente_toup:
                        print("Utente trovato:", utente_toup)
                        utente_updated = self.inserisci_dati_modifica()
                        self.validazione_up(utente_updated)
                        self.arricchisci_up(utente_updated)  # add "status":"modified","last_update":"timestamp"
                        if utente_updated:
                            self.modifica_dati(user_id_upd, utente_updated)
                            print("Utente modificato con successo.")
                        else:
                            print("Nessuna modifica effettuata.")
                    else:
                        print("Nessun utente trovato con l'ID specificato.")

                elif operazione == "EXIT":
                    running = False
                else:
                    print("Operazione non valida, riprova.")
            except ValueError as ve:
                print(ve)

    def validazione(self, utente):
        self.validator.valida(utente)

    def validazione_up(self, utente):
        self.validator.valida_up(utente)

    def calcola_num_utenti(self):
        return self.db_utenti.get_last_id()

    def arricchisci(self, utente, num_utenti):
        self.enricher.enrich(utente, num_utenti)

    def arricchisci_up(self, utente):
        self.enricher.enrich_up(utente)

    # Input da tastiera dati dell'utente
    def inserisci_id(self):
        return InputUser().inserisci_id()

    def inserisci_dati(self):
        return InputUser().inserisci_dati()

    def inserisci_dati_modifica(self):
        return InputUser().inserisci_dati_modifica()

    # CRUD OPERATIONS
    # Inserimento
    def inserisci_db(self, utente):
        self.db_utenti.insert_one(utente.__dict__)

    # Ricerca per id
    def ricerca_per_id(self, user_id):
        utente = self.db_utenti.find_by_id(user_id)
        if utente:
            print("Utente trovato:", utente)
        else:
            print("Nessun utente trovato con l'ID specificato.")

    # Visualizza tutti
    def visualizza_tutti(self):
        utenti = self.db_utenti.find()
        for utente in utenti:
            print(utente)

    # Cancellazione
    def cancella_per_id(self,  user_id):
        result = self.db_utenti.delete_by_id(user_id)
        if result.deleted_count > 0:
            print("Utente cancellato con successo.")
        else:
            print("Nessun utente trovato con l'ID specificato.")

    # Modifica
    def modifica_dati(self, user_id, modifiche):
        self.db_utenti.update_by_id(user_id, modifiche)
