# enrichment.py
from datetime import datetime


class Enricher:
    def enrich(self, utente, num_utenti):
        utente.int_id_utente = num_utenti + 1
        utente.date_creation = datetime.now().strftime("%d %B %Y")  # .strftime("%d-%m-%Y")

    def enrich_up(self, utente):
        utente['status'] = "modified"
        utente['last_update'] = datetime.now()
