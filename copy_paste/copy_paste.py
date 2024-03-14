from pymongo import MongoClient

url_start = 'mongodb://dbcreator:dbcreator@192.168.10.89:27017/?authMechanism=DEFAULT&authSource=admin'
db_start = 'SBDL10'
collection_start = 'CIB_CREED_fixed_match_Pietro'

url_dest = 'mongodb://localhost:27017/'
db_dest = 'TestAlessandro'
collection_dest = 'collection_test'


client_start = MongoClient(url_start)
filter={}

cursor_res = client_start[db_start][collection_start].find( filter=filter )

# cast a lista che contiene ogni singolo documento (dizionario)
lst_res = list(cursor_res)



client_dest = MongoClient(url_dest)
cursor_dest = client_dest[db_dest][collection_dest].insert_many(lst_res)
