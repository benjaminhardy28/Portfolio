from turtle import bgcolor
import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *
import sqlite3
from PIL import Image,ImageTk
import os

class KeyEditorMenu(ttk.LabelFrame):
    def __init__(self, parentWidget): 
        super().__init__(parentWidget, text="Edit Your JoySticks Key Configuration", bootstyle="dark")
        images_path = 'icons'
        self.parent = parentWidget
        self.currentAlt = 0
        self.currentKeyLayout = self.parent.dataUpdater.getKeyLayout()

        self.controlButtonsFrame = ttk.LabelFrame(self, text = "Control Buttons", bootstyle = "info")
        self.controlButtonsFrame.place(x=10,y=650, width=550, height=80)

        keyTextLabelFrame = ttk.LabelFrame(self, bootstyle="primary", text="Optional Special Keys")  
        keyList1 = list(self.parent.dataUpdater.specialKeysFormat.keys())[:15]

        self.keylistLabel1 = self.createListLabel(keyTextLabelFrame, keyList1)
        self.keylistLabel1.place(x=20,y=30) #650 200
        
        keyList2 = list(self.parent.dataUpdater.specialKeysFormat.keys())[15:30]
        self.keylistLabel2 = self.createListLabel(keyTextLabelFrame, keyList2)
        self.keylistLabel2.place(x=140,y=30)

        keyList3 = list(self.parent.dataUpdater.specialKeysFormat.keys())[30:45]
        self.keylistLabel3 = self.createListLabel(keyTextLabelFrame, keyList3)
        self.keylistLabel3.place(x=260,y=30)

        keyList4 = list(self.parent.dataUpdater.specialKeysFormat.keys())[45:60]
        self.keylistLabel4 = self.createListLabel(keyTextLabelFrame, keyList4)
        self.keylistLabel4.place(x=340,y=30)

        keyList5 = list(self.parent.dataUpdater.specialKeysFormat.keys())[60:]
        self.keylistLabel5 = self.createListLabel(keyTextLabelFrame, keyList5)
        self.keylistLabel5.place(x=400,y=30)
        
        keyTextLabelFrame.place(x=560, y=130, width=550, height=500) 

        self.EditConfigLabel = ttk.Label(
            self, 
            text="Edit Your JoyStick Key Configuration", 
            font=("Arial, 40"),
            bootstyle = "Primary"
            )
        self.EditConfigLabel.place(x=80,y=50)

        self.pinkJoyStickImage = ImageTk.PhotoImage(Image.open(os.path.join(images_path, "pinkJoyStick.jpeg")))
        self.joyTopLeft = ttk.Label(self, image=self.pinkJoyStickImage, font=("Arial", 13))
        self.joyTopRight = ttk.Label(self, image=self.pinkJoyStickImage, font=("Arial", 13))
        self.joyBotLeft = ttk.Label(self, image=self.pinkJoyStickImage, font=("Arial", 13))
        self.joyBotRight = ttk.Label(self, image=self.pinkJoyStickImage, font=("Arial", 13))

        self.TLLeft = ttk.Entry(self, bootstyle="info", width=5)
        self.TLRight = ttk.Entry(self, bootstyle="info", width=5)
        self.TLTop = ttk.Entry(self, bootstyle="info", width=5)
        self.TLBottom = ttk.Entry(self, bootstyle="info", width=5)

        self.TRLeft = ttk.Entry(self, bootstyle="info", width=5)
        self.TRRight = ttk.Entry(self, bootstyle="info", width=5)
        self.TRTop = ttk.Entry(self, bootstyle="info", width=5)
        self.TRBottom = ttk.Entry(self, bootstyle="info", width=5)

        self.BLLeft = ttk.Entry(self, bootstyle="info", width=5)
        self.BLRight = ttk.Entry(self, bootstyle="info", width=5)
        self.BLTop = ttk.Entry(self, bootstyle="info", width=5)
        self.BLBottom = ttk.Entry(self, bootstyle="info", width=5)

        self.BRLeft = ttk.Entry(self, bootstyle="info", width=5)
        self.BRRight = ttk.Entry(self, bootstyle="info", width=5)
        self.BRTop = ttk.Entry(self, bootstyle="info", width=5)
        self.BRBottom = ttk.Entry(self, bootstyle="info", width=5)

        self.joyTopLeft.place(x=80, y=200)
        self.joyTopRight.place(x=370, y=200)
        self.joyBotLeft.place(x=80, y=500)
        self.joyBotRight.place(x=370, y=500)

        self.TLLeft.place(x=20, y=220)
        self.TLRight.place(x=155, y=220)
        self.TLTop.place(x=90, y=170)
        self.TLBottom.place(x=90, y=275)

        self.TRLeft.place(x=310, y=220)
        self.TRRight.place(x=445, y=220)
        self.TRTop.place(x=380, y=170)
        self.TRBottom.place(x=380, y=275)

        self.BLLeft.place(x=20, y=520)
        self.BLRight.place(x=155, y=520)
        self.BLTop.place(x=90, y=470)
        self.BLBottom.place(x=90, y=575)

        self.BRLeft.place(x=310, y=520)
        self.BRRight.place(x=445, y=520)
        self.BRTop.place(x=380, y=470)
        self.BRBottom.place(x=380, y=575)

        self.altsMenuButton = ttk.Menubutton(self.controlButtonsFrame, text="Alt 1",bootstyle="info")
        self.altsMenuInside = tk.Menu(self.altsMenuButton)
        self.altsMenuButton.place(x=50,y=10)
        self.saveChangesButton = ttk.Button(self.controlButtonsFrame, bootstyle="outline", text="Save Changes", command=lambda:self.saveChanges())
        self.saveChangesButton.place(x=150,y=10)
       # self.toSettingsMenuButton = ttk.Button(self.controlButtonsFrame, text="Go Back to Main Menu", command=lambda:self.saveChanges())
        self.backButton = ttk.Button(self.controlButtonsFrame,  bootstyle="outline", text="Back", command = lambda: self.parent.hideOptionMenu())
        self.backButton.place(x=300, y=10)
        self.canSave = True
        self.saveOutputLabel = ttk.Label(self, text="", bootstyle="info")

        self.deleteConfigButton = ttk.Button(self.controlButtonsFrame, text="Delete Config", bootstyle="danger", command= lambda:self.deleteConfig())
        self.deleteConfigButton.place(x=380, y=10)

        self.creatAltDropDown()

    def createListLabel(self, keyTextLabelFrame, text):
        return ttk.Label(
            keyTextLabelFrame, 
            bootstyle="dark", 
            font=("Arial, 20"),
            text= '\n'.join(text)
        )

    def placeSelf(self):
        self.place(width=1190, height=760, x=230,y=5)

    def creatAltDropDown(self):
        alts =["Alt 1", "Alt 2", "Alt 3", "Alt 4"]
        for alt in alts:
            self.altsMenuInside.add_radiobutton(label=alt, command= lambda alt=alt: self.updateDropDownText(alt))
        self.altsMenuButton['menu'] = self.altsMenuInside
    
    def updateDropDownText(self, newMainText):
        self.currentAlt = (int(newMainText[4:]) - 1)
        match(self.currentAlt + 1):
            case 1:
                self.altsMenuButton.config(bootstyle="info")
            case 2:
                self.altsMenuButton.config(bootstyle="primary")
            case 3:
                self.altsMenuButton.config(bootstyle="warning")
            case 4:
                self.altsMenuButton.config(bootstyle="success")
        print(self.currentAlt)
        self.clearScreen()
        self.altsMenuButton.config(text=newMainText)  

    def checkIfAllowed(self, inputtedKey):
        if(inputtedKey != ""):
            return (inputtedKey in self.parent.dataUpdater.specialKeysFormat) if (len(inputtedKey) > 1) else True
        return False

    def saveInput(self, i, k, EntryBox):
        if(self.checkIfAllowed(EntryBox.get())):
            self.currentKeyLayout[i][self.currentAlt][k] = EntryBox.get()
            EntryBox.config(bootstyle="success")
        # elif(len(EntryBox.get()) == 0):
        #     self.canSave = True
        elif(len(EntryBox.get()) != 0): 
            EntryBox.config(bootstyle="danger")
            self.saveOutputLabel.config(text="Can not save, incorrect key entering format", bootstyle="danger")
            self.canSave = False



    def saveChanges(self):
        self.canSave = True
        self.saveOutputLabel.config(text="         The keys saved succesfully", bootstyle = "success")
        self.saveInput(0, 3, self.TLLeft) 
        self.saveInput(0, 0, self.TLRight)
        self.saveInput(0, 2, self.TLTop) 
        self.saveInput(0, 1, self.TLBottom)

        self.saveInput(1, 3, self.TRLeft)
        self.saveInput(1, 0, self.TRRight)
        self.saveInput(1, 2, self.TRTop)
        self.saveInput(1, 1, self.TRBottom)

        self.saveInput(2, 3, self.BLLeft)
        self.saveInput(2, 0, self.BLRight)
        self.saveInput(2, 2, self.BLTop)
        self.saveInput(2, 1, self.BLBottom)

        self.saveInput(3, 3, self.BRLeft)
        self.saveInput(3, 0, self.BRRight)
        self.saveInput(3, 1, self.BRTop)
        self.saveInput(3, 1, self.BRBottom)
        
        self.saveOutputLabel.place(x=140, y=380)
        print(self.currentKeyLayout)
        print(self.canSave)
        if(self.canSave):
            self.saveKeysToDatabase()

    def saveKeysToDatabase(self):
        listOfKeys = []
        config_info = self.parent.SettingsMenu.getLayoutConfigInfo()
        # print("config_info")
        # print(config_info)
        previousLayout = self.parent.dataUpdater.getUserLayout(config_info, self.currentAlt) 

        # print("previous:")
        # print(previousLayout)

        listOfKeys.append(self.TRTop.get())
        listOfKeys.append(self.TRLeft.get())
        listOfKeys.append(self.TRBottom.get())
        listOfKeys.append(self.TRRight.get())

        listOfKeys.append(self.TLTop.get())
        listOfKeys.append(self.TLLeft.get())
        listOfKeys.append(self.TLBottom.get())
        listOfKeys.append(self.TLRight.get())

        listOfKeys.append(self.BRTop.get())
        listOfKeys.append(self.BRLeft.get())
        listOfKeys.append(self.BRBottom.get())
        listOfKeys.append(self.BRRight.get())

        listOfKeys.append(self.BLTop.get())
        listOfKeys.append(self.BLLeft.get())
        listOfKeys.append(self.BLBottom.get())
        listOfKeys.append(self.BLRight.get())
    
        # print("listofkeys")
        # print(listOfKeys)
        for index, element in enumerate(listOfKeys):
            print(index)
            if(element != ''):
                previousLayout[index] = element

        newLayout = previousLayout
        # print("new:")
        # print(newLayout)

        self.updateConfigID(newLayout)

    def updateConfigID(self, listOfKeys):
        configName = self.parent.SettingsMenu.getLayoutConfigInfo()
        self.parent.dataUpdater.updateKeyFormat(self.currentAlt, listOfKeys, configName)

    def deleteConfig(self):
        # call the data updated to remove the configuration from the SQLite database
        configInfo = self.parent.SettingsMenu.getLayoutConfigInfo()
        print(configInfo)
        self.parent.dataUpdater.deleteUserConfig(configInfo)
        #exit out of the keyEditor Menu
        self.parent.hideOptionMenu()

    def clearScreen(self):
        self.TLLeft.delete(0,END)
        self.TLRight.delete(0,END)
        self.TLTop.delete(0,END)
        self.TLBottom.delete(0,END)
        self.TRLeft.delete(0,END)
        self.TRRight.delete(0,END)
        self.TRTop.delete(0,END)
        self.TRBottom.delete(0,END)
        self.BLLeft.delete(0,END)
        self.BLRight.delete(0,END)
        self.BLTop.delete(0,END)
        self.BLBottom.delete(0,END)
        self.BRLeft.delete(0,END)
        self.BRRight.delete(0,END)
        self.BRTop.delete(0,END)
        self.BRBottom.delete(0,END)
        
        self.TLLeft.config(bootstyle="info")
        self.TLRight.config(bootstyle="info")
        self.TLTop.config(bootstyle="info")
        self.TLBottom.config(bootstyle="info")
        self.TRLeft.config(bootstyle="info")
        self.TRRight.config(bootstyle="info")
        self.TRTop.config(bootstyle="info")
        self.TRBottom.config(bootstyle="info")
        self.BLLeft.config(bootstyle="info")
        self.BLRight.config(bootstyle="info")
        self.BLTop.config(bootstyle="info")
        self.BLBottom.config(bootstyle="info")
        self.BRLeft.config(bootstyle="info")
        self.BRRight.config(bootstyle="info")
        self.BRTop.config(bootstyle="info")
        self.BRBottom.config(bootstyle="info")

        self.saveOutputLabel.config(text="")



        


  

