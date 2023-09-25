from turtle import bgcolor
import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *
import sqlite3
from PIL import Image,ImageTk
import os


class WelcomeMenu(ttk.LabelFrame):
    def __init__(self, parentWidget):
        super().__init__(parentWidget, bootstyle="primary", text="Welcome Menu")
        self.parent = parentWidget
        self.logo = ImageTk.PhotoImage(Image.open(os.path.join("icons", "FG_Logo_Light.jpeg")))
        self.titleLabel = ttk.Label(self, image=self.logo)
        self.titleLabel.place(x=10, y=10) #places the title widget inside of the boardDisplay widget, which is packed inside the master widget which is the window called displayWindow
        self.welcomeLabel = ttk.Label(
            self,
            text = "Welcome to the Accessiboard learning App",
            font = ("Arial, 19"),
            bootstyle = "Primary"
            )
        self.welcomeLabel.place(x=30,y=235)

        self.mainTextFrame = ttk.LabelFrame(self, text="App Information",
            bootstyle = "Primary")
        self.mainTextFrame.place(x=20,y=270, width=410, height=300)

        self.mainTextLabel = ttk.Label(
            self.mainTextFrame,
            text = "Here is where you may find questions about this application. \nBelow is a list of different features of this tool.\n\nBoard View Only: This allows you to only view the needed \nfeatures to use the board on your computer.\n\nSettings Menu: This is where you have the option to change the\nkey configuration layout on the Accessiboard controller. You can\nselect an existing configuration or create a new one to edit or\nupload to the board.\n\nOptions Menu: This is where you can navigate between the\ndifferent menus, and also connect to the Accessiboard itself.\n\nFor more information about how the Accessiboard or this\napplication works, please see our website below.",
            font = ("Arial, 13"),
            bootstyle = "info"
            )
        self.mainTextLabel.place(x=10, y=10)


    def placeSelf(self):
        self.place(width=450, height=600, x=230,y=165)