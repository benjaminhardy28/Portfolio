from flask import current_app
# with current_app.app_context():
#     db = current_app.config['db']
from main import db

class SetNotification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    website_url = db.Column(db.String(150))
    notif_description = db.Column(db.String(150)) 
    notif_name =  db.Column(db.String(20)) 
    communication_prefs = db.Column(db.Integer) #integer value for email, text, or both
    websites_update = db.Column(db.BigInteger) #hash value for the websites html text