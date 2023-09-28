from flask import current_app
# with current_app.app_context():
#     db = current_app.config['db']
from main import db

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    setNotification_id = db.Column(db.Integer)
    date_time = db.Column(db.String(20))
    notif_description = db.Column(db.String(150)) 
    full_notification = db.Column(db.String(100))
    short_notification = db.Column(db.String(20))