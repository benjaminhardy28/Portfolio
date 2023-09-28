from bs4 import BeautifulSoup
from apscheduler.schedulers.background import BackgroundScheduler
import threading
from generator import NotificationGenerator
from checker import NotificationChecker
from web_searcher import WebSearcher
import hashlib
import requests
from datetime import date

class NotificationBuilder:
    #needs public id and notif id
    def __init__(self, notifInfo):
        self.user_input = notifInfo
        self.notificationChecker = NotificationChecker(notifInfo)
        self.newNotifGenerator = NotificationGenerator(notifInfo)

    #temp for testing
    def startMonitoringSchedule(self):
        scheduler = BackgroundScheduler()
        scheduler.add_job(self.check_if_update, 'interval', seconds=10)
        scheduler.start()


    #temp for testing
    def check_if_update(self):

        with open('new_web_text.txt') as f:
            lines = f.readlines()
        new_text = " ".join(lines)

        with open('previous_web_text.txt') as f:
            lines = f.readlines()
        previous_text = " ".join(lines)

        self.previous_hash = hashlib.sha256(previous_text.encode()).hexdigest()
        self.new_hash = hashlib.sha256(new_text.encode()).hexdigest()

        if self.new_hash != self.previous_hash:
            print("The website has been updated!")
            notif = self.newNotifGenerator.getNotif(new_text, previous_text)
            print(notif)
            self.add_notif(notif)
        else:
            print("The website has not been updated!")
        self.previous_hash = self.new_hash
    
    def add_notif(self, notif):
        #API call to add notif 
        '''
            NEEDED INFO
            user id
            set notif id
        '''
        data = {
            "public_id" : "c88867a1-c091-4a5f-97ec-5102978ada9b",
            "date_time" : str(date.today()),
            "notif_description" : "A notification to be made for any tests",
            "full_notification" : notif,
            "short_notification" : notif
        }
        response = requests.post("http://127.0.0.1:5000/notification_from_python/1/4", json=data)
        print(response.text)
        if response.status_code == 200:
            print("The notification has been added")
        else:
            print("The notification was not added")


    # new_notification = Notification(
    #     user_id = current_user.id,
    #     setNotification_id = setNotif_id, 
    #     date_time= data['date_time'],
    #     notif_description= data['notif_description'],
    #     full_notification= data['full_notification'],
    #     short_notification= data['short_notification']
    # )




        

