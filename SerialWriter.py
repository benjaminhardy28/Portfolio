import serial.tools.list_ports
import json

class SerialWriter(serial.Serial):

    def __init__(self, baudrate, portName):
        super().__init__(baudrate=baudrate, port=portName)
  

    def updateArduinoConfig(self, arrayLayout):
        for eachAlt in arrayLayout:
            print(eachAlt)
            super().write((json.dumps(eachAlt) + '\n').encode())  # Encode the string as bytes and send each row with an end line character at the end. This makes sure the arduino only reads 2d array for each individual joystick at a time
