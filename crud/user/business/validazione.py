# validazione.py
class Validator:
    def valida(self, utente):
        if utente.int_eta <= 5 or utente.int_eta >= 80:
            raise ValueError("L'età deve essere compresa tra 5 e 80 anni.")

        if utente.str_nome == '' or utente.str_cognome == '':
            raise ValueError("Nome e cognome non possono essere vuoti")

        if not utente.str_nome[0].isupper() or not utente.str_cognome[0].isupper():
            raise ValueError("Il nome e il cognome devono iniziare con una maiuscola.")


    def valida_up(self, utente):
        if 'int_eta' in utente and (utente['int_eta'] <= 5 or utente['int_eta'] >= 80):
            raise ValueError("L'età deve essere compresa tra 5 e 80 anni.")

        if 'str_nome' in utente and ('str_nome' not in utente or utente['str_nome'] == '' or utente['str_cognome'] == ''):
            raise ValueError("Nome e cognome non possono essere vuoti")

        if 'str_nome' in utente and ('str_nome' not in utente or not utente['str_nome'][0].isupper() or not utente['str_cognome'][0].isupper()):
            raise ValueError("Il nome e il cognome devono iniziare con una maiuscola.")
