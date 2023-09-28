from web_searcher import WebSearcher
from apscheduler.schedulers.background import BackgroundScheduler

class NotificationChecker():
    def __init__(self, url):
        self.newWebSearcher = WebSearcher(url)

    def startMonitoringSchedule(self):
        scheduler = BackgroundScheduler()
        scheduler.add_job(self.newWebSearcher.monitorWebsiteChanges(self), 'interval', seconds=5)
        scheduler.start()

    ## access database previous hash value
    