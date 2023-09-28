from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import uuid 
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import jwt
from functools import wraps
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = '65f09dd54282479fa0a11f7b94d0f4cf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/benjaminhardy/CUSTOM_NOTIFICATION_WEBSITE/flask-server/notify_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False;


cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000", "supports_credentials": True}})

db = SQLAlchemy(app)

# dataBase(app)
# register_blueprints(app)

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

@app.route('/user', methods=['POST'])
def create_user():
    new_user_data = request.get_json()
    print(new_user_data)
    hashed_password = generate_password_hash(new_user_data['password'], method= "sha256") #SHA-256 is a widely used cryptographic hash function known for its security properties
    new_user = User(
        public_id=str(uuid.uuid4()), 
        email=new_user_data['email'], 
        phone_number=new_user_data['phone_number'], 
        password=hashed_password, 
        admin=False
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message" : "new user created"})

@app.route('/user', methods=['GET'])
def get_all_user():
    user = User.query.all()
    output = []
    for user in user:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['email'] = user.email
        user_data['phone_number'] = user.phone_number
        user_data['password'] = user.password
        user_data['admin'] = user.admin
        output.append(user_data)
    return jsonify({'user' : output})

@app.route('/user/<public_id>', methods=['GET'])
def get_user(public_id):
    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify({'message' : 'User not found'})
    user_data = {}
    user_data['public_id'] = user.public_id
    user_data['email'] = user.email
    user_data['phone_number'] = user.phone_number
    user_data['password'] = user.password
    user_data['admin'] = user.admin
    return jsonify({'user' : user_data})

@app.route('/user/<public_id>', methods=['DELETE'])
def delete_user(public_id):
    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify({'message' : 'User not found', 'public_id' :public_id })
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message' : 'User has been deleted'})


@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization #gets authorization information
    if not auth or not auth.username or not auth.password:
        return make_response('Missing Username or Password', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})
    user = User.query.filter_by(email=auth.username).first()
    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'}) #user does not exist
    if check_password_hash(user.password, auth.password): #checks the user password with the password passed in with the request
        token = jwt.encode({ 
            #JWT token payload 
            'public_id' : user.public_id, #public id to recognize user
            'expiration' : str(datetime.datetime.utcnow() + datetime.timedelta(minutes=45)) #expiration time for token
        },
            app.config['SECRET_KEY'] #secret key to show valid jwt
        ) #tokens public id is set, expiration of 45 minutes, and app.config['SECRET_KEY'] is used to encode the token
        #return jsonify({'token' : jwt.decode(token)})
        return jsonify({'token' : token, 'name' : auth.username})
    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'}) #password does not check out

@app.route('/all_setNotifications', methods=['GET'])
def get_allSetNotifications():
    notifications = SetNotification.query.all()
    output = []
    for notif in notifications:
        notif_data = {}
        notif_data['id'] = notif.id
        notif_data['user_id'] = notif.user_id
        notif_data['website_url'] = notif.website_url
        notif_data['notif_description'] = notif.notif_description
        notif_data['communication_prefs'] = notif.communication_prefs
        notif_data['websites_update'] = notif.websites_update
        output.append(notif_data)
    return jsonify({'All-Notifications' : output})


@app.route('/set_notification', methods=['POST'])
@token_required
def create_notification(current_user):
    data = request.get_json()
    new_setNotification = SetNotification(
        user_id=current_user.id, 
        website_url=data['website_url'], 
        notif_description=data['notif_description'], 
        communication_prefs=data['communication_prefs'], 
        websites_update=data['websites_update']
    )
    db.session.add(new_setNotification)
    db.session.commit()
    return jsonify({'message' : 'Notification added', 'user' : current_user.id})

@app.route('/set_notification', methods=['GET'])
@token_required
def get_setNotifications(current_user):
    notifications = SetNotification.query.filter_by(user_id=current_user.id).all()
    output = []
    for notif in notifications:
        notif_data = {}
        notif_data['id'] = notif.id
        notif_data['user_id'] = notif.user_id
        notif_data['website_url'] = notif.website_url
        notif_data['notif_description'] = notif.notif_description
        notif_data['communication_prefs'] = notif.communication_prefs
        notif_data['websites_update'] = notif.websites_update
        output.append(notif_data)
    return jsonify({'SetNotification' : output, 'user' : current_user.id})

# @app.route('/all_setNotifications_from_python', methods=['GET'])
# def get_allSetNotifications():
#     notifications = SetNotification.query.all()
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
#     return jsonify({'All-Notifications' : output})


@app.route('/set_notification/<notif_id>', methods=['DELETE'])
@token_required
def delete_notification(current_user, notif_id):
    notification = SetNotification.query.filter_by(user_id=current_user.id, id=notif_id).first()
    if not notification:
        return jsonify({'message' : 'Notification was not found',  'user_id' : current_user.id, 'notif_id' : notif_id})
    db.session.delete(notification)
    db.session.commit()
    return jsonify({'messgae' : "notification was deleted", 'notif_id' : notif_id})

@app.route('/notifications/<setNotif_id>', methods=['POST'])
@token_required
def add_notifications(current_user, setNotif_id):
    data = request.get_json()
    new_notification = Notification(
        user_id = current_user.id,
        setNotification_id = setNotif_id, 
        date_time= data['date_time'],
        notif_description= data['notif_description'],
        full_notification= data['full_notification'],
        short_notification= data['short_notification']
    )
    db.session.add(new_notification)
    db.session.commit()
    return jsonify({'message' : 'Notification added', 'user' : current_user.id, 'notif_id' : setNotif_id})
#http://127.0.0.1:5000/notification_from_python/3
@app.route('/notification_from_python/<int:user_id>/<int:setNotif_id>', methods=['POST'])
def add_notifications_from_python(user_id, setNotif_id):
    data = request.get_json()
    current_user = User.query.filter_by(id=user_id).first()
    new_notification = Notification(
        user_id = user_id, 
        setNotification_id = setNotif_id,
        date_time= data['date_time'],
        notif_description= data['notif_description'],
        full_notification= data['full_notification'],
        short_notification= data['short_notification']
    )
    db.session.add(new_notification)
    db.session.commit()
    return jsonify({'message' : 'Notification added', 'user' : user_id, 'notif_id' : setNotif_id})
    #return jsonify({'message' : 'Notification added', 'user' : current_user.id, 'notif_id' : setNotif_id})


@app.route('/notifications/<setNotif_id>', methods=['GET'])
@token_required
def get_notifications(current_user, setNotif_id):
    all_notifications = Notification.query.filter_by(user_id=current_user.id,setNotification_id=setNotif_id).all()
    notifs_content = []
    for notif in all_notifications:
        data = {}
        # data['public_id'] = 
        data['Date/Time'] = notif.date_time
        data['notif_description'] = notif.notif_description
        data['full_notification'] = notif.full_notification
        data['short_notification'] = notif.short_notification
        notifs_content.append(data)
    if not all_notifications:
        return jsonify({'message' : 'There are no notifications',  'user_id' : current_user.id, 'notif_id' : setNotif_id})
    return jsonify({'notifications' : notifs_content,  'user_id' : current_user.id, 'notif_id' : setNotif_id})

if __name__ == '__main__':
    # notif_builder = ThreadCreator()
    # notif_builder_thread = threading.Thread(target=notif_builder.startNotifBuilder)
    app.run(debug=True)

