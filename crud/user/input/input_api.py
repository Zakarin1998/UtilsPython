import json
from typing import Union

from bson import json_util
from fastapi import FastAPI, HTTPException, Response

from DB.dati_utente import DBDatiUtente

app = FastAPI()

# CRUD

# GET
@app.get("/users/{user_id}")
def get_user(user_id: str):
    db_utenti = DBDatiUtente()
    print("Sono qui")
    user = db_utenti.find_by_id(user_id)
    if user:
        return user
    else:
        return Response(
            content=json.dumps({"Errore": "Nessun utente trovato con questo nome"}),
            status_code=404
        )

@app.get("/users/")
def get_users_by_params(nome: Union[str, None] = None, cognome: Union[str, None] = None, eta: Union[int, None] = None):
    db_utenti = DBDatiUtente()
    if nome is not None or cognome is not None or eta is not None:
        users = list(db_utenti.find_by_name(nome))
        if users:
            return Response(
                content=json.dumps(users, default=json_util.default),
                status_code=200
            )
        else:
            return Response(
                content=json.dumps({"Errore": "Nessun utente trovato con questo nome"}),
                status_code=404
            )

    else:
        users = list(db_utenti.find())
        return Response(
            content=json.dumps(users, default=json_util.default),
            status_code=200
        )

# Create
@app.post("/users/")
async def create_user(user_data: dict):
    db_utenti = DBDatiUtente()
    user_id = db_utenti.insert_one(user_data).inserted_id
    return {"id": str(user_id), **user_data}


# Delete
@app.delete('/users/{user_id}')
async def delete_user(user_id: int):
    db_utenti = DBDatiUtente()
    result = db_utenti.delete_by_id(user_id)
    if result.deleted_count > 0:
        print("Utente cancellato con successo.")
    else:
        print("Nessun utente trovato con l'ID specificato.")

#Update
@app.post('/users/{user_id}')
async def update_user(user_id: int):
    db_utenti = DBDatiUtente()
    result = db_utenti.update_by_id(user_id)
    if result.modified_count > 0:
        print("Utente modificato con successo.")
    else:
        print("Nessun utente trovato con l'ID specificato.")

