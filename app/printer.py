import serial

from .utils import FakeConnexion


class Printer:
    OK = "ok"

    def __init__(self, fake: bool = False):
        if fake is True:
            self.connexion = FakeConnexion()
        else:
            self.connexion = serial.Serial("/dev/ttyUSB0", 115200)

    def write(self, command: str):
        self.connexion.write(f"{command}\n".encode())

    def read(self) -> str:
        response = self.connexion.readline()
        return response.decode().strip().lower()

    def cmd(self, command) -> bool:
        """
        General command function
        command example: "G1 X10 Y18 Z10 E10"
        """
        self.write(command)
        response: str | None = None

        # Wait until command has finished
        while response != Printer.OK:
            response = self.read()
            # time.sleep(0.1)  # Wait for 0.1 second
            print(response)

        return True
