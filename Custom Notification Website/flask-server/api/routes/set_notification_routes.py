from flask import Blueprint, jsonify, Flask, request, make_response, current_app
from main import SetNotification
# from app import db
from main import token_required
with current_app.app_context():
    app = current_app
    db = current_app.config['db']

set_notification_bp = Blueprint('set_notification_bp', __name__)

@set_notification_bp.route('/set_notification', methods=['POST'])
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

@set_notification_bp.route('/set_notification', methods=['GET'])
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

@set_notification_bp.route('/set_notification/<notif_id>', methods=['DELETE'])
@token_required
def delete_notification(current_user, notif_id):
    notification = SetNotification.query.filter_by(user_id=current_user.id, id=notif_id).first()
    if not notification:
        return jsonify({'message' : 'Notification was not found',  'user_id' : current_user.id, 'notif_id' : notif_id})
    db.session.delete(notification)
    db.session.commit()
    return jsonify({'messgae' : "notification was deleted", 'notif_id' : notif_id})





