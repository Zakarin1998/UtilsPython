from DB.mongo_abstract import DBAbstract


class DBDatiUtente(DBAbstract):
    def __init__(self):
        super().__init__()

    def collection_name(self):
        return "test"
