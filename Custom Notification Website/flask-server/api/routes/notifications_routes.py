from flask import Blueprint, jsonify, Flask, request, make_response, current_app
from main import SetNotification
from main import Notification
# from app import db
from utils.auth import token_required
with current_app.app_context():
    app = current_app
    db = current_app.config['db']

notifications_bp = Blueprint('notifications_bp', __name__)

@notifications_bp.route('/notifications/<setNotif_id>', methods=['POST'])
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


@notifications_bp.route('/notifications/<setNotif_id>', methods=['GET'])
@token_required
def get_notifications(current_user, setNotif_id):
    all_notifications = Notification.query.filter_by(user_id=current_user.id,setNotification_id=setNotif_id).all()
    notifs_content = []
    for notif in all_notifications:
        data = {}
        data['Date/Time'] = notif.date_time
        data['notif_description'] = notif.notif_description
        data['full_notification'] = notif.full_notification
        data['short_notification'] = notif.short_notification
        notifs_content.append(data)
    if not all_notifications:
        return jsonify({'message' : 'There are no notifications',  'user_id' : current_user.id, 'notif_id' : setNotif_id})
    return jsonify({'notifications' : notifs_content,  'user_id' : current_user.id, 'notif_id' : setNotif_id})
