from turtle import bgcolor
import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *
from PIL import Image,ImageTk
import os
import json


class SettingsMenu(ttk.LabelFrame):
    def __init__(self, parentWidget): 
        super().__init__(parentWidget, bootstyle="primary", text="Create new Custom Config")
        self.parent = parentWidget
        self.logo = ImageTk.PhotoImage(Image.open(os.path.join("icons", "FG_Logo_Light.jpeg")))
        self.titleLabel = ttk.Label(self, image=self.logo)
        self.titleLabel.place(x=10, y=10) #places the title widget inside of the boardDisplay widget, which is packed inside the master widget which is the window called displayWindow
        self.fNameLabel = ttk.Label(self, text="Enter in first name", width=15)
        self.configNameLabel = ttk.Label(self, text="Enter in config name", width=15)
        self.firstNameEntry = ttk.Entry(self, bootstyle="primary")
        self.configNameEntry = ttk.Entry(self, bootstyle="primary")
        self.submitConfigButton = ttk.Button(self, text="Create Custom Config", bootstyle="warning", command=lambda:self.userLogins())
        self.welcomeLabel = ttk.Label(self, text=" ", bootstyle="primary")
        #self.editKeysButton = ttk.Button(self, text="Edit Keys Configuration", command=lambda:self.changeToKeyEditorMenu())

        self.configsMenuButton = ttk.Menubutton(self, text="Change Layout Config", bootstyle="success")
        self.configsMenuInside = tk.Menu(self.configsMenuButton)
        self.configsMenuInside.add_radiobutton(label="Create New Config", command = lambda: self.createNewConfig())
        self.configsMenuButton['menu'] = self.configsMenuInside

        self.editConfigButton = ttk.Button(self, bootstyle="outline", text="Edit Layout", command= lambda:self.changeToKeyEditorMenu())
        self.uploadConfigButton = ttk.Button(self, bootstyle="outline", text="Use Layout", command= lambda:self.prepareConfigUpload())
        #self.editConfigButton.place(x=300, y=250)

        #set config info to default
        # self.userName = ""
        # self.configName = ""

        self.configsMenuButton.place(x=170,y=250)

        self.selectConfigText = ttk.Label(
            self, 
            text="Select from the drop down menu to change the configuration", 
            font=("Arial, 15"),
            bootstyle = "success"
            )

        self.selectConfigText.place(x=20, y=220)

        self.creatConfigDropDown()


    def placeSelf(self):
        self.place(width=450, height=600, x=230,y=165)

    def createNewConfig(self):
        self.configSelected("Creating new config")
        self.editConfigButton.place_forget()
        self.uploadConfigButton.place_forget()
        self.fNameLabel.place(x=20, y=300)
        self.firstNameEntry.place(x=160, y=300)
        self.configNameLabel.place(x=20, y=350)
        self.configNameEntry.place(x=160, y=350)
        self.submitConfigButton.place(x=180, y=400)

    def hideNewConfigOption(self):
        self.fNameLabel.place_forget()
        self.firstNameEntry.place_forget()
        self.configNameLabel.place_forget()
        self.configNameEntry.place_forget()
        self.submitConfigButton.place_forget()

    def creatConfigDropDown(self):
        configs = self.parent.dataUpdater.getConfigs()
        # self.configsMenuInside.delete()
        self.configsMenuInside = tk.Menu(self.configsMenuButton)
        self.configsMenuInside.add_radiobutton(label="Create New Config", command = lambda: self.createNewConfig())
        self.configsMenuButton['menu'] = self.configsMenuInside
        #self.configsMenuInside.option_clear()
        for config in configs:
            self.configsMenuInside.add_radiobutton(label=config, command= lambda config=config: self.configSelected(config))
    
    def configSelected(self, newMainText):
        self.configName = newMainText
        self.configsMenuButton.config(text=newMainText)
        # info = newMainText.split(" ")
        print("newmain: " + str(newMainText))
        self.userName = newMainText[0]
        self.configName = newMainText[1]
        # print(info[0])
        # print(info[1])
        #self.changeToKeyEditorMenu()
        if newMainText != "Creating new config":
            self.editConfigButton.place(x=330, y=250)
            self.uploadConfigButton.place(x=30, y=250)
            print("not" )
        else:
            print("is")
        self.hideNewConfigOption()
        
    def userLogins(self):
        self.userName = self.firstNameEntry.get()
        self.configName = self.configNameEntry.get()
        self.firstNameEntry.delete(0,END)
        self.configNameEntry.delete(0,END)
        self.firstNameEntry.place_forget()
        self.configNameEntry.place_forget()
        self.fNameLabel.place_forget()
        self.configNameLabel.place_forget()
        self.configNameEntry.place_forget()
        self.submitConfigButton.place_forget()
        userEntry = [self.userName, self.configName]
        self.parent.dataUpdater.updateTableUser(userEntry)
        self.changeToKeyEditorMenu()

    def showControllerButtons(self):
        self.gameViewButton.place(x=20, y=330)
        self.editKeysButton.place(x=200, y=330)

    def changeToGameView(self):
        self.parent.changeToGame()

    def changeToKeyEditorMenu(self):
        self.parent.changeToKeyEditor()

    def getLayoutConfigInfo(self):
        print("info:")
        print(self.userName)
        print(self.configName)
        config_info = [self.userName, self.configName]
        return config_info
    
    def prepareConfigUpload(self): #formatts the user layouts i
        layout = self.parent.dataUpdater.getTotalUserLayout(self.getLayoutConfigInfo()) #Gets layouts from database, 2d array
        for rowIndex, row in enumerate(layout): #Goes through each row of the 2d array
            for index, element in enumerate(row): #goes though each column in each row of the 2d array
                if len(element) > 1: #checks if the element has a length of greater than one, meaning it is a special key 
                    layout[rowIndex][index] = str(self.parent.dataUpdater.specialKeysString[element]) #converts the special key name into its correct decimal value
        totalLayout3D = [[[None for _ in range(4)] for _ in range(4)] for _ in range(4)] #
        for index, element in enumerate(layout):
            new2Darray = [element[i:i+4] for i in range(0, 16, 4)]
            totalLayout3D[index] = new2Darray
        reformattedTotalLayout = list(zip(*totalLayout3D)) #reformatts the 2d array so that the rows become columns and the columns become rows. in other words, each array previously held all of the keys per alt, and now each array holds all of the keys per joystick. This is the needed format for the arudino program
        self.parent.serialWriter.updateArduinoConfig(reformattedTotalLayout)
        
        #need to reformat the layout so that each row is per joystick and not alt
        # [['1', '1', '1', '1'], ['1', '1', '1', '1'], ['1', '1', '1', '1'], ['1', '1', '1', '1']]
        # [['2', '2', '2', '2'], ['2', '2', '2', '2'], ['2', '2', '2', '2'], ['2', '2', '2', '2']]
        # [['3', '3', '3', '3'], ['3', '3', '3', '3'], ['3', '3', '3', '3'], ['3', '3', '3', '3']]
        # [['4', '4', '4', '4'], ['4', '4', '4', '4'], ['4', '4', '4', '4'], ['4', '4', '4', '4']]
        #becomes:
        # [(['1', '1', '1', '1'], ['2', '2', '2', '2'], ['3', '3', '3', '3'], ['4', '4', '4', '4']), 
        #  (['1', '1', '1', '1'], ['2', '2', '2', '2'], ['3', '3', '3', '3'], ['4', '4', '4', '4']), 
        #  (['1', '1', '1', '1'], ['2', '2', '2', '2'], ['3', '3', '3', '3'], ['4', '4', '4', '4']), 
        #  (['1', '1', '1', '1'], ['2', '2', '2', '2'], ['3', '3', '3', '3'], ['4', '4', '4', '4'])]
                                      
        



    
