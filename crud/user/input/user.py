# Definizione DTO Utente
class User:
    def __init__(self, str_nome, str_cognome, int_eta=18, int_id_utente=None, date_creation=None ):
        self.str_nome = str_nome
        self.str_cognome = str_cognome
        self.int_eta = int_eta
        self.int_id_utente = int_id_utente
        self.date_creation = date_creation

    def __str__(self):
        return f"Nome: {self.str_nome}, Cognome: {self.str_cognome}, Età: {self.int_eta}"

    # Meglio di __dict__ , perché posso gestire oggetti nidificati
    def to_dict(self):
        return {
            "str_nome": self.str_nome,
            "str_cognome": self.str_cognome,
            "int_eta": self.int_eta,
            "int_id_utente": self.int_id_utente,
            "date_creation": self.date_creation # isodate
        }
