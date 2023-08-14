import sqlite3
import json
import ast

class DataUpdater():
    def __init__(self): 
        self.port = ""
        self.allKeysLayout = [
            [["   w", "   a", "   s", "   d"], ["   e", "shft", "  ctlr", "del"],["scup", "   9", "scbt", "scd"],["   1", "   2", "   3", "   4"]],
            [["   q", "   e", "   r", "   t"], ["   j", "   k", "  l", "  z"], [" F1", " F2", " F3", " F4"],["   5", "   6", "   7", "   8"]],
            [["   y", "   u", "   i", "   o"], ["   x", "   c", "   v", "   b"],[" F5", " F6", " F7", " F8"],["alt", "tab", "insr", "bksp"]],
            [["   p", "   f", "   g", "   h"], ["   n", "   m", "esc", "caps"], [" F9", "F10", "F11", "F12"], ["  ~", "rtrn", "home", "end"]]
        ]
        self.specialKeysFormat = {
            "Left Control": "LCtrl",
            "Left Shift": "LShft",
            "Left Alt": "LAlt",
            "Left GUI": "LGUI",
            "Right Control": "RCtrl",
            "Right Shift": "RShft",
            "Right Alt": "RAlt",
            "Right GUI": "RGUI",
            "Tab": " Tab",
            "Caps Lock": "CpLk",
            "Backspace": "Bksp",
            "Return": "Rtrn",
            "Menu": "Menu",
            "Insert": "Insrt",
            "Delete": "Delt",
            "Home": "Home",
            "End": " End",
            "Page Up": "PgUp",
            "Page Down": "PgDn",
            "Up Arrow": "UpAr",
            "Down Arrow": "DnAr",
            "Left Arrow": "LtAr",
            "Right Arrow": "RtAr",
            "Num Lock": " NmL",
            "KP Slash": "KPSL",
            "KP Asterisk": "KPAS",
            "KP Minus": "KPMI",
            "KP Plus": "KPPL",
            "KP Enter": "KPEN",
            "KP 1": "   1",
            "KP 2": "   2",
            "KP 3": "   3",
            "KP 4": "   4",
            "KP 5": "   5",
            "KP 6": "   6",
            "KP 7": "   7",
            "KP 8": "   8",
            "KP 9": "   9",
            "KP 0": "   0",
            "KP Dot": "KPDO",
            "Escape": "Escp",
            "F1": "  F1",
            "F2": "  F2",
            "F3": "  F3",
            "F4": "  F4",
            "F5": "  F5",
            "F6": "  F6",
            "F7": "  F7",
            "F8": "  F8",
            "F9": "  F9",
            "F10": " F10",
            "F11": " F11",
            "F12": " F12",
            "F13": " F13",
            "F14": " F14",
            "F15": " F15",
            "F16": " F16",
            "F17": " F17",
            "F18": " F18",
            "F19": " F19",
            "F20": " F20",
            "F21": " F21",
            "F22": " F22",
            "F23": " F23",
            "F24": " F24",
            "Print Screen": "PrSc",
            "Scroll Lock": "PrCl",
            "Pause": "Paus"
        }
        self.specialKeysDecimal = {
            128 : "Left Control",
            129 : "Left Shift",
            130 : "Left Alt",
            131 : "Left GUI",
            132 : "Right Control",
            133 : "Right Shift",
            134 : "Right Alt",
            135 : "Right GUI",
            179 : "Tab",
            193 : "Caps Lock",
            178 : "Backspace",
            176 : "Return",
            237 : "Menu",
            209 : "Insert",
            212 : "Delete",
            210 : "Home",
            213 : "End",
            211 : "Page Up",
            214 : "Page Down",
            218 : "Up Arrow",
            217 : "Down Arrow",
            216 : "Left Arrow",
            215 : "Right Arrow",
            219 : "Num Lock",
            220 : "KP Slash",
            221 : "KP Asterisk",
            222 : "KP Minus",
            223 : "KP Plus",
            224 : "KP Enter",
            225 : "KP 1",
            226 : "KP 2",
            227 : "KP 3",
            228 : "KP 4",
            229 : "KP 5",
            230 : "KP 6",
            231 : "KP 7",
            232 : "KP 8",
            233 : "KP 9",
            234 : "KP 0",
            235 : "KP Dot",
            177 : "Escape",
            194 : "F1",
            195 : "F2",
            196 : "F3",
            197 : "F4",
            198 : "F5",
            199 : "F6",
            200 : "F7",
            201 : "F8",
            202 : "F9",
            203 : "F10",
            204 : "F11",
            205 : "F12",
            240 : "F13",
            241 : "F14",
            242 : "F15",
            243 : "F16",
            244 : "F17",
            245 : "F18",
            246 : "F19",
            247 : "F20",
            248 : "F21",
            249 : "F22",
            250 : "F23",
            251 : "F24",
            206 : "Print Screen",
            207 : "Scroll Lock",
            208 :"Pause",
        }
        self.specialKeysString =  {v: k for k, v in self.specialKeysDecimal.items()}
        #self.createTable()

    #MIGHT NOT NEED
    def getKeyLayout(self): #returns the current user layout

        return self.allKeysLayout


    def setKeyLayout(self, newKeyLayout):

        self.allKeysLayout = newKeyLayout
    

    def createTable(self): #creates the table used. Only called once

        dbConnection = sqlite3.connect('custom_key_layouts.db')
        cursor = dbConnection.cursor()
        cursor.execute("""CREATE TABLE key_layouts (
            first_name text,    
            config_name text,
            keys_formatted_alt1 text,
            keys_formatted_alt2 text,
            keys_formatted_alt3 text,
            keys_formatted_alt4 text
        )
        """)
        
        dbConnection.commit()
        dbConnection.close()
    

    def getConfigs(self):
        dbConnection = sqlite3.connect('custom_key_layouts.db')
        cursor = dbConnection.cursor()
        cursor.execute("SELECT first_name, config_name FROM key_layouts")
        allLayouts = cursor.fetchall()
        dbConnection.commit()
        dbConnection.close()
        return allLayouts


    def getUserLayout(self, config_info, alt):

        print("alt")
        print(alt)
        dbConnection = sqlite3.connect('custom_key_layouts.db')
        cursor = dbConnection.cursor()
        #cursor.execute("SELECT keys_formatted_alt1, keys_formatted_alt2, keys_formatted_alt3, keys_formatted_alt4 text FROM key_layouts WHERE first_name = ? AND config_name = ?" , (config_info[0], config_info[1]))
        match(alt):
            case 0: 
                cursor.execute("SELECT keys_formatted_alt1 FROM key_layouts WHERE first_name = ? AND config_name = ?" , (config_info[0], config_info[1]))
            case 1:
                cursor.execute("SELECT keys_formatted_alt2 FROM key_layouts WHERE first_name = ? AND config_name = ?" , (config_info[0], config_info[1]))
            case 2:
                cursor.execute("SELECT keys_formatted_alt3 FROM key_layouts WHERE first_name = ? AND config_name = ?" , (config_info[0], config_info[1]))
            case 3:
                cursor.execute("SELECT keys_formatted_alt4 FROM key_layouts WHERE first_name = ? AND config_name = ?" , (config_info[0], config_info[1]))

        userLayoutFromDB_tuple = cursor.fetchone()
        print("output tuple straight from database")
        print(userLayoutFromDB_tuple)
        print("first element in tuple - string")
        print(str(userLayoutFromDB_tuple[0]))
        #array = ast.literal_eval(userLayoutFromDB_tuple[0])
        array = json.loads(userLayoutFromDB_tuple[0])
        return array
    
    def getTotalUserLayout(self, config_info):
        dbConnection = sqlite3.connect('custom_key_layouts.db')
        cursor = dbConnection.cursor()
        cursor.execute("SELECT keys_formatted_alt1, keys_formatted_alt2, keys_formatted_alt3, keys_formatted_alt4 FROM key_layouts WHERE first_name = ? AND config_name = ?" , (config_info[0], config_info[1]))
        userLayoutFromDB_tuple = cursor.fetchone()
        #combinedLayoutArray = ast.literal_eval(userLayoutFromDB_tuple[0]) + ast.literal_eval(userLayoutFromDB_tuple[1]) + ast.literal_eval(userLayoutFromDB_tuple[2]) + ast.literal_eval(userLayoutFromDB_tuple[3])
        combinedLayoutArray = [
            json.loads(userLayoutFromDB_tuple[0]),
            json.loads(userLayoutFromDB_tuple[1]),
            json.loads(userLayoutFromDB_tuple[2]),
            json.loads(userLayoutFromDB_tuple[3]),
        ]
        print("combined array from db:")
        print(combinedLayoutArray)
        return combinedLayoutArray

    def updateTableUser(self, update):

        dbConnection = sqlite3.connect('custom_key_layouts.db')
        cursor = dbConnection.cursor()
        #Check if user already exists
        cursor.execute("SELECT * from key_layouts WHERE first_name = ? AND config_name = ?" , (update[0], update[1]))
        checkingResult = cursor.fetchone()
        emptyArray = ['', '', '', '', '', '', '', '','', '', '', '','', '', '', '',]
        serializedEmptyArray = json.dumps(emptyArray)
        # "Empty" = json.dumps(emptyArray)
        if checkingResult:
            print("config already exists")
        else:
            print('config does not exist')
            cursor.execute("INSERT INTO key_layouts VALUES (:f_name, :c_name, :null_key_layout1, :null_key_layout2, :null_key_layout3, :null_key_layout4)",
                    {
                        'f_name': update[0],
                        'c_name': update[1],
                        'null_key_layout1': serializedEmptyArray,
                        'null_key_layout2': serializedEmptyArray,
                        'null_key_layout3': serializedEmptyArray,
                        'null_key_layout4': serializedEmptyArray
                    })
        cursor.execute("SELECT *, oid FROM key_layouts")
        allPeople = cursor.fetchall()
        print("all people")
        print(allPeople)
        dbConnection.commit()
        dbConnection.close()


    def deleteUserConfig(self, config_info):

        print(config_info)
        dbConnection = sqlite3.connect('custom_key_layouts.db')
        cursor = dbConnection.cursor()
        query = "DELETE FROM key_layouts WHERE first_name = ? AND config_name = ?"
        cursor.execute(query, (config_info[0], config_info[1]))
        allPeople = cursor.fetchall()
        print("selected person: ")
        print(allPeople)

        cursor.execute("SELECT *, oid FROM key_layouts")
        allPeople = cursor.fetchall()
        print("new group ")
        print(allPeople)

        dbConnection.commit()
        dbConnection.close()


    def updateKeyFormat(self, alt, keysList, configName):
        #keysString = str(keysList)
        keysString = json.dumps(keysList)
        print("keys string")
        print(keysString)
        #keysString = ', '.join(keysList)
        #keysString = keysString.replace("'", "")
        dbConnection = sqlite3.connect('custom_key_layouts.db')
        cursor = dbConnection.cursor()
        match(alt):
            case 0: 
                cursor.execute("UPDATE key_layouts SET keys_formatted_alt1 = ? WHERE first_name = ? AND config_name = ? ", (keysString, configName[0], configName[1]))
            case 1:
                cursor.execute("UPDATE key_layouts SET keys_formatted_alt2 = ? WHERE first_name = ? AND config_name = ? ", (keysString, configName[0], configName[1]))
            case 2:
                cursor.execute("UPDATE key_layouts SET keys_formatted_alt3 = ? WHERE first_name = ? AND config_name = ? ", (keysString, configName[0], configName[1]))
            case 3:
                cursor.execute("UPDATE key_layouts SET keys_formatted_alt4 = ? WHERE first_name = ? AND config_name = ? ", (keysString, configName[0], configName[1]))
        print("keys data columns:")
        cursor.execute("SELECT *, oid FROM key_layouts")
        allPeople = cursor.fetchall()
        print(allPeople)
        dbConnection.commit()
        dbConnection.close()
        

    def updateKeyConfig(self):
        pass


    def setPort(self, newPort):
        self.port = newPort


    def getPort(self):
        return self.port