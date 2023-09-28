import requests
import json
import threading
from builder import NotificationBuilder


class ThreadCreator():
    def __init__(self) -> None:
        self.startThreads()


    def startThreads(self):
        #access API and start a thread for each setNotification
        #iterate through list of API calls
        setNotifications = requests.get('http://127.0.0.1:5000/all_setNotifications')
        print(setNotifications.text)
        newNotifBuilder = NotificationBuilder("test")
        notificationCheckerThread = threading.Thread(target=newNotifBuilder.startMonitoringSchedule())
        notificationCheckerThread.daemon = True
        notificationCheckerThread.start()
        for setNotification in setNotifications:
            pass


if __name__ == "__main__":
    ThreadCreator()
    while True:
        pass