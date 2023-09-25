from turtle import bgcolor
import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *

class Alt(ttk.Frame):
    def __init__(self, parentWidget, image, joyCharacters): 
        super().__init__(parentWidget)

        self.joyStickImage = image
        self.characters = joyCharacters
        #self.joyStickFrame = ttk.Frame(self.window)
        #make all 4 joysticks
        self.joyTopLeft = ttk.Label(self, image=self.joyStickImage, font=("Arial", 13))
        self.joyTopRight = ttk.Label(self, image=self.joyStickImage, font=("Arial", 13))
        self.joyBotLeft = ttk.Label(self, image=self.joyStickImage, font=("Arial", 13))
        self.joyBotRight = ttk.Label(self, image=self.joyStickImage, font=("Arial", 13))
        #Charcters for 4 joy sticks. labels are TL=top left, TR=top right, BL=bottom left, BR=bottom right
        self.TLtop = ttk.Label(self, text=self.characters[0][0], font=("Arial", 13))
        self.TLleft = ttk.Label(self, text=self.characters[0][1], font=("Arial", 13))
        self.TLright = ttk.Label(self, text=self.characters[0][3], font=("Arial", 13))
        self.TLbottom = ttk.Label(self, text=self.characters[0][2], font=("Arial", 13))
        self.TRtop = ttk.Label(self, text=self.characters[1][0], font=("Arial", 13))
        self.TRleft = ttk.Label(self, text=self.characters[1][1], font=("Arial", 13))
        self.TRright = ttk.Label(self, text=self.characters[1][3], font=("Arial", 13))
        self.TRbottom = ttk.Label(self, text=self.characters[1][2], font=("Arial", 13))
        self.BLtop = ttk.Label(self, text=self.characters[2][0], font=("Arial", 13))
        self.BLleft = ttk.Label(self, text=self.characters[2][1], font=("Arial", 13))
        self.BLright = ttk.Label(self, text=self.characters[2][3], font=("Arial", 13))
        self.BLbottom = ttk.Label(self, text=self.characters[2][2], font=("Arial", 13))
        self.BRtop = ttk.Label(self, text=self.characters[3][0], font=("Arial", 13))
        self.BRleft = ttk.Label(self, text=self.characters[3][1], font=("Arial", 13))
        self.BRright = ttk.Label(self, text=self.characters[3][3], font=("Arial", 13))
        self.BRbottom = ttk.Label(self, text=self.characters[3][2], font=("Arial", 13))

        self.joyTopLeft.place(x=33, y=40)
        self.joyTopRight.place(x=130, y=40)
        self.joyBotLeft.place(x=33, y=200)
        self.joyBotRight.place(x=130, y=200)

        self.TLtop.place(x=35, y=20)
        self.TLleft.place(x=0, y=55)
        self.TLright.place(x=72, y=55)
        self.TLbottom.place(x=35, y=95)

        self.TRtop.place(x=130, y=20)
        self.TRleft.place(x=105, y=55)
        self.TRright.place(x=170, y=55)
        self.TRbottom.place(x=133, y=95)

        self.BLtop.place(x=35, y=180)
        self.BLleft.place(x=0, y=215)
        self.BLright.place(x=72, y=215)
        self.BLbottom.place(x=35, y=255)

        self.BRtop.place(x=130, y=180)
        self.BRleft.place(x=105, y=215)
        self.BRright.place(x=170, y=215)
        self.BRbottom.place(x=133, y=255)
        self.place(width=200, height=300, x=0,y=250)


    def updateJoySticks(self):
        self.tkraise()

        
