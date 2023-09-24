from serialWatcher import *
from GUI import *
import ttkbootstrap as ttk
import threading
from DataUpdater import DataUpdater

class App():
    def __init__(self):
            displayWindow = ttk.Window(title="FG Display",themename="cosmo", resizable=(False, False)) # creates window with title, theme, and allowing it to be resized
            displayWindow.geometry("700x770") # sets size of window
            dataUpdater = DataUpdater()
            GUI = boardDisplay(displayWindow, dataUpdater) # creates instance of boardDisplay widget and ttk.Frame widget as it is a subclass. Passing the root widget which is the window
            try:
                #'/dev/cu.usbmodemHIDFG1 - Arduino Due'
                #'/dev/cu.usbmodem12301 - Arduino Due Prog. Port'
                #port = '/dev/cu.usbmodem12301'
                port = '/dev/cu.usbmodemHIDFG1'
                serialReader = serialData(2000000, GUI, dataUpdater, port)
                controllerThread = threading.Thread(target=lambda: serialReader.watchSerial())
                controllerThread.daemon = True
                controllerThread.start()
            except serial.serialutil.SerialException:
                print("cannot access board")
            GUI.pack(fill=BOTH, expand=YES) 
            #print("second thread starting")
            displayWindow.mainloop()

if __name__ == "__main__":
    App()

     