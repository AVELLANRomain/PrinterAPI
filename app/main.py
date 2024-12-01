# upload the file on the raspberry: scp -r ../API micro@192.168.1.141:EnderLab
# activate virtual environement: source test/bin/activate
# lancer l'api: uvicorn API.main:app --host 0.0.0.0 --port 8000 --reload

from fastapi import FastAPI

from .printer import Printer

printer = Printer(fake=True)
app = FastAPI()


@app.get("/")
def main():
    return {"Hello": "World"}


@app.get("/cmd")
def command(cmd: str):
    response = printer.cmd(cmd)
    return {"response": response}
