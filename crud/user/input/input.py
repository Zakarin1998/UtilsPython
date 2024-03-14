from input.user import User


class InputUser:

    @staticmethod
    def inserisci_dati():
        str_input_user = input("Inserisci: Nome Cognome (eta): ")
        lst_fields = str_input_user.split(" ")
        int_dimensioni_input = len(lst_fields)
        if int_dimensioni_input < 2:
            raise ValueError("Inserire almeno nome e cognome")
        elif int_dimensioni_input == 2:
            return User(lst_fields[0], lst_fields[1])
        else:
            return User(lst_fields[0], lst_fields[1], int(lst_fields[2]))

    @staticmethod
    def inserisci_id():
        user_id = input("Inserisci l'ID dell'utente da cercare: ")
        return user_id

    def inserisci_dati_modifica(self):
        modifiche = {}
        while True:
            campo = input("Inserisci il nome del campo da modificare (exit per terminare): ")
            if campo.upper() == 'EXIT':
                break
            valore = input(f"Inserisci il nuovo valore per '{campo}': ")
            modifiche[campo] = valore

        return modifiche

