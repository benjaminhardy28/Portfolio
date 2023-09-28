from flask import current_app
from main import db
# with current_app.app_context():
#     db = current_app.config['db']

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) #user id for the database
    public_id = db.Column(db.String(50), unique=True) #public user id to be encrypted in token
    email = db.Column(db.String(50))
    phone_number = db.Column(db.String(15))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)