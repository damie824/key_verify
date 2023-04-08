import json
from typing import Union
from fastapi import FastAPI

app = FastAPI()

def keyVerify(keyID, userIP):
    result = 0
    with open('./public/key_db.json') as db:
        keyDB = json.load(db)
    for i in keyDB:
        if i['key'] == keyID:
            result = 1
            i['ip'] == userIP
    with open('./public/key_db.json', 'w') as db:
        json.dump(keyDB, db, indent=2)
    if result == 1:
        return True
    else:
        return False

@app.get("/")
def read_root():
    return {"message": "Lexip API Server"}


@app.get("/verify")
def read_item(keyID: Union[str, None] = None, userIP: Union[str, None] = None):
    if keyVerify(keyID, userIP):
        return {"result":"success", "message":"successfully verified key by {}.".format(userIP)}
    else:
        return {"result":"false", "message":"verify failed."}
    
