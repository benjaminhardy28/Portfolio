from flask import Blueprint, jsonify, Flask, request, make_response, current_app
from werkzeug.security import generate_password_hash, check_password_hash
# from models.set_notification import SetNotification
# from models.notification import Notification
import jwt
import datetime
from main import User
with current_app.app_context():
    app = current_app


login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/login', methods=['POST'])
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
