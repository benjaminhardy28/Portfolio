import serial.tools.list_ports

class serialData(serial.Serial):

    def __init__(self, baudrate, display, dataUpdater, portName):
        super().__init__(baudrate=baudrate, port=portName)
        self.setAlt = 1
        self.setCombine = 0
        self.display = display
        self.portsList = serial.tools.list_ports.comports()
        self.portNames = []
        self.readPortNames()
        self.dataUpdater = dataUpdater


    def readPortNames(self):
        for singlePort in self.portsList:
            self.portNames.append(str(singlePort))
        print(self.portNames)
        self.display.OptionsMenu.creatPortDropDown(self.portNames)


    def watchSerial(self):

        while True:
            try:
                if super().in_waiting: #if there is data ready to be read
                    infoSentBinary = super().readline()
                    infosentString = infoSentBinary.decode('utf-8').rstrip() #convert binary to unicode string
                    print("info from port " + infosentString)
                    self.display.interpretGameData(infosentString) #call methed which interprets the data
            except UnicodeDecodeError as e:
                self.display.interpretGameData("combC*") #call methed which interprets the data
                print("There has been an error in reading from the game controller")
        
        

