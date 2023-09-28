from flask import Blueprint, jsonify, Flask, request, make_response, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from main import User
import uuid 

with current_app.app_context():
    db = current_app.config['db']
    app = current_app

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/user', methods=['POST'])
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

@user_bp.route('/user', methods=['GET'])
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

@user_bp.route('/user/<public_id>', methods=['GET'])
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

@user_bp.route('/user/<public_id>', methods=['DELETE'])
def delete_user(public_id):
    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify({'message' : 'User not found', 'public_id' :public_id })
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message' : 'User has been deleted'})