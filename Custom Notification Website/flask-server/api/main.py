from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import uuid 
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import jwt
from functools import wraps
from blueprint_setup import register_blueprints

app = Flask(__name__)


cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000", "supports_credentials": True}})

db = SQLAlchemy(app)
app.config['SECRET_KEY'] = '65f09dd54282479fa0a11f7b94d0f4cf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/benjaminhardy/CUSTOM_NOTIFICATION_WEBSITE/flask-server/notify_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False;
app.config['db'] = db
# dataBase(app)
register_blueprints(app)




# app.register_blueprint(user_bp)
# app.register_blueprint(set_notification_bp)
# app.register_blueprint(notifications_bp)


    # app.config['SECRET_KEY'] = '65f09dd54282479fa0a11f7b94d0f4cf'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/benjaminhardy/CUSTOM_NOTIFICATION_WEBSITE/flask-server/notify_database.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False;
 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) #user id for the database
    public_id = db.Column(db.String(50), unique=True) #public user id to be encrypted in token
    email = db.Column(db.String(50))
    phone_number = db.Column(db.String(15))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)

class SetNotification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    website_url = db.Column(db.String(150))
    notif_description = db.Column(db.String(150)) 
    notif_name =  db.Column(db.String(20)) 
    communication_prefs = db.Column(db.Integer) #integer value for email, text, or both
    websites_update = db.Column(db.BigInteger) #hash value for the websites html text

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    setNotification_id = db.Column(db.Integer)
    date_time = db.Column(db.String(20))
    notif_description = db.Column(db.String(150)) 
    full_notification = db.Column(db.String(100))
    short_notification = db.Column(db.String(20))


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message' : 'Token is missing'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message' : 'Token is invalid'}), 401
        return f(current_user, *args, **kwargs)
    return decorated

# @app.route('/user', methods=['POST'])
# def create_user():
#     new_user_data = request.get_json()
#     print(new_user_data)
#     hashed_password = generate_password_hash(new_user_data['password'], method= "sha256") #SHA-256 is a widely used cryptographic hash function known for its security properties
#     new_user = User(
#         public_id=str(uuid.uuid4()), 
#         email=new_user_data['email'], 
#         phone_number=new_user_data['phone_number'], 
#         password=hashed_password, 
#         admin=False
#     )
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify({"message" : "new user created"})

# @app.route('/user', methods=['GET'])
# def get_all_user():
#     user = User.query.all()
#     output = []
#     for user in user:
#         user_data = {}
#         user_data['public_id'] = user.public_id
#         user_data['email'] = user.email
#         user_data['phone_number'] = user.phone_number
#         user_data['password'] = user.password
#         user_data['admin'] = user.admin
#         output.append(user_data)
#     return jsonify({'user' : output})

# @app.route('/user/<public_id>', methods=['GET'])
# def get_user(public_id):
#     user = User.query.filter_by(public_id=public_id).first()
#     if not user:
#         return jsonify({'message' : 'User not found'})
#     user_data = {}
#     user_data['public_id'] = user.public_id
#     user_data['email'] = user.email
#     user_data['phone_number'] = user.phone_number
#     user_data['password'] = user.password
#     user_data['admin'] = user.admin
#     return jsonify({'user' : user_data})

# @app.route('/user/<public_id>', methods=['DELETE'])
# def delete_user(public_id):
#     user = User.query.filter_by(public_id=public_id).first()
#     if not user:
#         return jsonify({'message' : 'User not found', 'public_id' :public_id })
#     db.session.delete(user)
#     db.session.commit()
#     return jsonify({'message' : 'User has been deleted'})


# @app.route('/login', methods=['POST'])
# def login():
#     auth = request.authorization #gets authorization information
#     if not auth or not auth.username or not auth.password:
#         return make_response('Missing Username or Password', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})
#     user = User.query.filter_by(email=auth.username).first()
#     if not user:
#         return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'}) #user does not exist
#     if check_password_hash(user.password, auth.password): #checks the user password with the password passed in with the request
#         token = jwt.encode({ 
#             #JWT token payload 
#             'public_id' : user.public_id, #public id to recognize user
#             'expiration' : str(datetime.datetime.utcnow() + datetime.timedelta(minutes=45)) #expiration time for token
#         },
#             app.config['SECRET_KEY'] #secret key to show valid jwt
#         ) #tokens public id is set, expiration of 45 minutes, and app.config['SECRET_KEY'] is used to encode the token
#         #return jsonify({'token' : jwt.decode(token)})
#         return jsonify({'token' : token, 'name' : auth.username})
#     return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'}) #password does not check out

# @app.route('/set_notification', methods=['POST'])
# @token_required
# def create_notification(current_user):
#     data = request.get_json()
#     new_setNotification = SetNotification(
#         user_id=current_user.id, 
#         website_url=data['website_url'], 
#         notif_description=data['notif_description'], 
#         communication_prefs=data['communication_prefs'], 
#         websites_update=data['websites_update']
#     )
#     db.session.add(new_setNotification)
#     db.session.commit()
#     return jsonify({'message' : 'Notification added', 'user' : current_user.id})

# @app.route('/set_notification', methods=['GET'])
# @token_required
# def get_setNotifications(current_user):
#     notifications = SetNotification.query.filter_by(user_id=current_user.id).all()
#     output = []
#     for notif in notifications:
#         notif_data = {}
#         notif_data['id'] = notif.id
#         notif_data['user_id'] = notif.user_id
#         notif_data['website_url'] = notif.website_url
#         notif_data['notif_description'] = notif.notif_description
#         notif_data['communication_prefs'] = notif.communication_prefs
#         notif_data['websites_update'] = notif.websites_update
#         output.append(notif_data)
#     return jsonify({'SetNotification' : output, 'user' : current_user.id})

# @app.route('/set_notification/<notif_id>', methods=['DELETE'])
# @token_required
# def delete_notification(current_user, notif_id):
#     notification = SetNotification.query.filter_by(user_id=current_user.id, id=notif_id).first()
#     if not notification:
#         return jsonify({'message' : 'Notification was not found',  'user_id' : current_user.id, 'notif_id' : notif_id})
#     db.session.delete(notification)
#     db.session.commit()
#     return jsonify({'messgae' : "notification was deleted", 'notif_id' : notif_id})

# @app.route('/notifications/<setNotif_id>', methods=['POST'])
# @token_required
# def add_notifications(current_user, setNotif_id):
#     data = request.get_json()
#     new_notification = Notification(
#         user_id = current_user.id,
#         setNotification_id = setNotif_id, 
#         date_time= data['date_time'],
#         notif_description= data['notif_description'],
#         full_notification= data['full_notification'],
#         short_notification= data['short_notification']
#     )
#     db.session.add(new_notification)
#     db.session.commit()
#     return jsonify({'message' : 'Notification added', 'user' : current_user.id, 'notif_id' : setNotif_id})


# @app.route('/notifications/<setNotif_id>', methods=['GET'])
# @token_required
# def get_notifications(current_user, setNotif_id):
#     all_notifications = Notification.query.filter_by(user_id=current_user.id,setNotification_id=setNotif_id).all()
#     notifs_content = []
#     for notif in all_notifications:
#         data = {}
#         data['Date/Time'] = notif.date_time
#         data['notif_description'] = notif.notif_description
#         data['full_notification'] = notif.full_notification
#         data['short_notification'] = notif.short_notification
#         notifs_content.append(data)
#     if not all_notifications:
#         return jsonify({'message' : 'There are no notifications',  'user_id' : current_user.id, 'notif_id' : setNotif_id})
#     return jsonify({'notifications' : notifs_content,  'user_id' : current_user.id, 'notif_id' : setNotif_id})


#eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwdWJsaWNfaWQiOiI0YjU5MDJlNy1kOWNjLTRjMzEtOGNlYi0yNGY2NGVlYTBlZWUiLCJleHBpcmF0aW9uIjoiMjAyMy0wNy0yOSAxODo0NDo0OC4zNzQ1NjkifQ.qXJi8JKyf5wgqrndLSCi1IGTQg1k92_5mOCG7pfao5w

#test public id: 9699d047-215f-4bac-9476-163465c16b34
#    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwdWJsaWNfaWQiOiI0YjU5MDJlNy1kOWNjLTRjMzEtOGNlYi0yNGY2NGVlYTBlZWUiLCJleHBpcmF0aW9uIjoiMjAyMy0wNy0yOCAyMzo0MzozMC44NjkxNjAifQ.nd3bjUvvhuoQ2ooy0WDX5n-01LaN4qlJ48B_ka6mBis"
# { {"email" : "benjatestDELETE", "phone_number" : "1234567890", "password" : "test"}
#     "user": [
#         {
#             "admin": false,
#             "email": "benjatest",
#             "password": "sha256$neNuTXUKfoat1PEX$2d60a329d80fb15b5d4e11d75f005fca6a99ff88648f02eec99416bab9245b27",
#             "phone_number": "1234567890",
#             "public_id": "9699d047-215f-4bac-9476-163465c16b34"
#         }
#     ]
# }

#     .tables
# notifications  user    


# {
#     "SetNotification": [
#         {
#             "communication_prefs": 1,
#             "id": 1,
#             "notif_description": "about the abcs",
#             "user_id": 1,
#             "website_url": "abcd.com",
#             "websites_update": "None"
#         }
#     ],
#     "user": 1
# }


#def startNotifBuilder():


if __name__ == '__main__':
    #notif_builder_thread = threading.Thread(target=startNotifBuilder)
    app.run(debug=True)


