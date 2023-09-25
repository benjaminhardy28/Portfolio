import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *
from ttkbootstrap import Style
from PIL import Image,ImageTk
from Alt import Alt
import time

class OptionsMenu(ttk.LabelFrame):
    def __init__(self, parentWidget): 
        super().__init__(parentWidget, bootstyle="warning", text="Options Menu")
        self.parent = parentWidget
        self.portsMenuButton = ttk.Menubutton(self, text="Select the controller", bootstyle="success")
        self.portsMenuInside = tk.Menu(self.portsMenuButton)
        self.portsMenuButton.place(x=85,y=10)
        self.settingsButton = ttk.Button(self, text="Settings Menu", command=lambda:self.parent.showSettingsMenu())
        self.settingsButton.place(x=170, y=70)
        self.gameViewOnlyButtom = ttk.Button(self, text="Game View Only", bootstyle="info", command=lambda:self.parent.changeToGameViewOnly())
        self.gameViewOnlyButtom.place(x=30, y=70)
        self.WelcomeMenuButton = ttk.Button(self, text="Welcome Menu", command=lambda:self.parent.showWelcomeMenu())
        self.WelcomeMenuButton.place(x=300, y=70)

        self.place(x=235, y=10, width=450, height=140)

    
    def creatPortDropDown(self, stringPorts):
        for port in stringPorts:
            self.portsMenuInside.add_radiobutton(label=port, command= lambda port=port: self.updateDropDownText(port))
        self.portsMenuButton['menu'] = self.portsMenuInside
    
    def updateDropDownText(self, newMainText):
        self.portsMenuButton.config(text=newMainText)
        self.parent.GameView.displayController() 