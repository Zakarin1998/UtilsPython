from abc import ABC, abstractmethod
from pymongo import MongoClient

MONGO_CLIENT = "mongodb+srv://admin:Password12345@iconic.15l5wtp.mongodb.net/"
MONGO_DB = "TestAlessandro"


class DBAbstract(ABC):

    def __init__(self):
        self.mongo_client = None
        self.mongo_db = None

    # CRUD
    def find(self):
        return self.collection().find()

    def insert_one(self, document):
        return self.collection().insert_one(document)

    def find_by_id(self, indice):
        return self.collection().find_one({"int_id_utente": int(indice)})

    def find_by_name(self, nome):
        return self.collection().find({"str_nome": nome})

    def delete_by_id(self, indice):
        return self.collection().delete_one({"int_id_utente": int(indice)})

    def get_last_id(self):
        last_user = self.collection().find_one(sort=[("int_id_utente", -1)])
        return last_user['int_id_utente'] if last_user else 0

    def update_by_id(self, indice, modifiche):
        try:
            result = self.collection().update_one({'int_id_utente': int(indice)}, {'$set': modifiche})
            return result.modified_count
        except Exception as e:
            print("Si è verificato un errore durante l'aggiornamento:", e)
            return 0

    # Connessione dinamica costruendo l'accesso alla collection
    def collection(self):
        return self.db()[self.collection_name()]

    def db(self):
        return self.client()[self.db_name()]

    def db_name(self):
        self.mongo_db = MONGO_DB
        return self.mongo_db

    def client(self):
        self.mongo_client = MongoClient(MONGO_CLIENT)
        return self.mongo_client

    @abstractmethod
    def collection_name(self):
        pass
