# upload the file on the raspberry: scp -r ../PrinterAPI micro@192.168.1.141:EnderLab
# conect to raspberry ssh micro@192.168.1.141
# activate virtual environement: source test/bin/activate
# lancer l'api: uvicorn PrinterAPI.app.main:app --host 0.0.0.0 --port 5000 --reload

from fastapi import FastAPI

from .printer import Printer

import RPi.GPIO as GPIO
from time import sleep

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)  # 11=GPIO17

pwm = GPIO.PWM(11, 60)
pwm.start(0)

printer = Printer(fake=True)
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
    pwm.ChangeDutyCycle(9)  # 0°
    sleep(1)
    pwm.ChangeDutyCycle(7.5)  # -45°
    sleep(1)
    pwm.ChangeDutyCycle(9)  # 0°
    sleep(1)

    print("eject")
    return {"response": "OK"}
