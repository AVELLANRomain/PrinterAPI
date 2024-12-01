#upload the file on the raspberry: scp -r ../API micro@192.168.1.141:EnderLab
#activate virtual environement: source test/bin/activate
# lancer l'api: uvicorn API.main:app --host 0.0.0.0 --port 8000 --reload
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/cmd")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}