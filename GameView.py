import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *
from ttkbootstrap import Style
from PIL import Image,ImageTk
from Alt import Alt
import time
import os



class GameView(ttk.LabelFrame):
    def __init__(self, parentWidget): 
        super().__init__(parentWidget, bootstyle="info", text="GameView")
        self.parent = parentWidget
        images_path ='icons'
        
        #Create all Images
        self.previousAlt = 1
        #title image
        self.logo = ImageTk.PhotoImage(Image.open(os.path.join(images_path, "FG_Logo_Dark.png")))
        self.titleLabel = ttk.Label(self, image=self.logo)
        #Joy stick images
        self.blueJoyStickImage = ImageTk.PhotoImage(Image.open(os.path.join(images_path, "blueJoyStick.png")))
        self.purpleJoyStickImage = ImageTk.PhotoImage(Image.open(os.path.join(images_path, "purpleJoyStick.png")))
        self.orangeJoyStickImage = ImageTk.PhotoImage(Image.open(os.path.join(images_path, "orangeJoyStick.png")))
        self.greenJoyStickImage = ImageTk.PhotoImage(Image.open(os.path.join(images_path, "greenJoyStick.png")))
        #set a variable holding alt set to 0
        self.closeMainMenuButton = ttk.Button(self, text="Back To Settings", bootstyle="info", width=15, command=lambda:self.back())

        #Create 4 Alt objects, passing the image of the joystick, and the characters
        #create and place all buttons
         
        self.altButton1 = ttk.Button(self, text="Alt 1 ", bootstyle="info", width=15)
        self.altButton2 = ttk.Button(self, text="Alt 2", bootstyle="primary", width=15)
        self.altButton3 = ttk.Button(self, text="Alt 3", bootstyle="warning", width=15)
        self.altButton4 = ttk.Button(self, text="Alt 4", bootstyle="success", width=15)

        #combine button and flood guage
        self.combineButton = ttk.Button(self, width=13, text="Combine: 0/3", bootstyle = "secondary") #Lamda function was added since I had an error where the command would be called only when the button was instantiated
        self.combineGauge = ttk.Floodgauge(
            bootstyle="secondary",
            font=(None, 10, 'bold'),
            value=0,
            length=160,
            maximum=3,
            )
        self.combineCharLabel = ttk.Label(self, font=(None, 20, 'bold'), text="")
        self.altButton1.place(x=15, y=115)
        self.altButton2.place(x=15, y=150)
        self.altButton3.place(x=15, y=185)
        self.altButton4.place(x=15, y=220)
        self.combineButton.place(x=20, y=555)
        self.combineGauge.place(x=18, y=615, height=15) 
        self.combineCharLabel.place(x=5, y=660)
        self.titleLabel.place(x=0, y=0) #places the title widget inside of the boardDisplay widget, which is packed inside the master widget which is the window called displayWindow
        self.place(x=5,y=5, width=210,height=760)

    def back(self):
        self.closeMainMenuButton.place_forget()
        self.parent.showOptionMenu()

    def changeToKeyEditorMenu(self):
        self.parent.changeToKeyEditor()

    def displayController(self):
        self.alt1 = Alt(self, self.purpleJoyStickImage, [["   w", "   a", "   s", "   d"], ["   e", "shft", "  ctlr", "del"],["scup", "   9", "scbt", "scd"],["   1", "   2", "   3", "   4"]])
        self.alt2 = Alt(self, self.blueJoyStickImage, [["   q", "   e", "   r", "   t"], ["   j", "   k", "  l", "  z"], [" F1", " F2", " F3", " F4"],["   5", "   6", "   7", "   8"]])
        self.alt3 = Alt(self, self.orangeJoyStickImage, [["   y", "   u", "   i", "   o"], ["   x", "   c", "   v", "   b"],[" F5", " F6", " F7", " F8"],["alt", "tab", "insr", "bksp"]])
        self.alt4 = Alt(self, self.greenJoyStickImage, [["   p", "   f", "   g", "   h"], ["   n", "   m", "esc", "caps"], [" F9", "F10", "F11", "F12"], ["  ~", "rtrn", "home", "end"]])

    def placeReturnButton(self):
        self.closeMainMenuButton.place(x=15, y=700)

    def updateCombineDisplay(self, combineNummber):
        if(combineNummber == 0):
            self.combineGauge.configure(value=0)
            self.combineCharLabel.configure(text="")
            time.sleep(.1)
        else:
            if self.combineGauge.variable.get() >= 2:
                self.combineGauge.configure(value=3)
            else:
                self.combineGauge.step(1)
        self.combineButton.config(text = "Combine: " + str(self.combineGauge.variable.get()) + "/3")

    def updateCombineCharsDisplay(self, addedCharacter):
        currentCharacters = self.combineCharLabel.cget("text") 
        newCombinedCharacters = currentCharacters + "   " + addedCharacter
        self.combineCharLabel.config(text=newCombinedCharacters)
    
    def updateAltDisplay(self, newAlt):
        match newAlt:
            case 1:
                self.alt1.updateJoySticks()
            case 2:
                self.alt2.updateJoySticks()
            case 3:
                self.alt3.updateJoySticks()
            case 4:
                self.alt4.updateJoySticks()