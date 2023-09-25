import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap import Style
from Alt import Alt
from SettingsMenu import SettingsMenu
from GameView import GameView
from KeyEditorMenu import KeyEditorMenu
from OptionsMenu import OptionsMenu
from WelcomeMenu import WelcomeMenu
from SerialWriter import SerialWriter

class boardDisplay(ttk.Frame):  #create a class for a frame which inherits ttkbootstrap Frame, which is a class that inherits tkinter
    def __init__(self, master, dataUpdater): #initializer method, passing self and master which is the window called displayWindow 
        super().__init__(master)    #call superclass initilizer, passing master which will set the Frame widgets parent to be the window called displayWindow
        self.window = master
        self.style = Style()
        self.dataUpdater = dataUpdater
        self.WelcomeMenu = WelcomeMenu(self)
        self.GameView = GameView(self)
        self.OptionsMenu = OptionsMenu(self)
        self.SettingsMenu = SettingsMenu(self)
        self.KeyEditorMenu = KeyEditorMenu(self)
        self.setAlt = 1
        self.SettingsMenu.placeSelf()
        self.WelcomeMenu.placeSelf()
        #port = '/dev/cu.usbmodem12301'
        # port = '/dev/cu.usbmodemHIDFG1'
        # self.serialWriter = SerialWriter(2000000, port)

    def hideOptionMenu(self):
        print("forget option")
        self.SettingsMenu.creatConfigDropDown()
        self.KeyEditorMenu.place_forget()
        self.window.geometry("700x770")

    def changeToGameViewOnly(self):
        self.window.geometry("220x770")
        self.GameView.placeReturnButton()

    def showOptionMenu(self):
        print("dnenfeubf")
        self.window.geometry("700x770")

    def showSettingsMenu(self):
        self.SettingsMenu.creatConfigDropDown()
        self.SettingsMenu.tkraise()

    def changeToKeyEditor(self):
        self.KeyEditorMenu.placeSelf()
        self.KeyEditorMenu.clearScreen()
        self.KeyEditorMenu.tkraise()
        self.window.geometry("1450x770")

    def showWelcomeMenu(self):
        self.WelcomeMenu.tkraise()

    ## move to different class
    def interpretGameData(self, info):
        data = info[0:5] #get first 5 characters which tell what the data is
        print(data)
        match data:
            case "alt_#":   #data sent has heading "alt_#" to mean it represents a new alt number
                nextAlt = info[5:6]
                if nextAlt != self.setAlt:
                    #print(nextAlt)
                    self.GameView.updateAltDisplay(int(nextAlt))
                    #self.after(100, self.display.updateAltDisplay(nextAlt))
                    self.setAlt = nextAlt
            case "comb#":   #data sent has heading "comb#" to mean it represents a new combine number
                newCombine = int(info[5:END])
                if newCombine > 127: #any number above 127 is not part of the ASCII table and must be sent to dataset
                    self.GameView.updateCombineDisplay(self.dataUpdater.specialKeysDecimal(newCombine)) #sent the decimal number as a key to the specialKeysDecimal dictionary to get the name of the key
                else:
                    self.GameView.updateCombineDisplay(newCombine)
            case "combC":   #data sent has a heading "combC" to mean it represent a new combine character
                print(info[5])
                self.GameView.updateCombineCharsDisplay(info[5])
                # showcharacter method(character)
            case _:
                print(data)

    # def uploadConfig(self, layoutArray):
    #     self.serialWriter.updateArduinoConfig(layoutArray)


    def setPortNames(self, portNames):
        #for eachPort in portNames:
         #   self.SettingsMenu.addPortName()
        pass

