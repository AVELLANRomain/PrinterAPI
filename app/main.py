# upload the file on the raspberry: scp -r ../PrinterAPI micro@192.168.1.141:EnderLab
# activate virtual environement: source test/bin/activate
# lancer l'api: uvicorn PrinterAPI.app.main:app --host 0.0.0.0 --port 5000 --reload

from fastapi import FastAPI

from .printer import Printer

printer = Printer(fake=False)
app = FastAPI()


@app.get("/")
def main():
    return {"Hello": "World"}


@app.get("/cmd")
def command(cmd: str):
    success = printer.cmd(cmd)
    if success:
        return {"response": cmd}
    return {"response": "error"}


@app.get("/eject")
def eject():
    print("eject")
    return {"response": "OK"}
