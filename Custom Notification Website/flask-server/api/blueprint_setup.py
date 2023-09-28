# blueprint_setup.py
from flask import Flask
from routes.login_route import login_bp
from routes.user_routes import user_bp
from routes.set_notification_routes import set_notification_bp
from routes.notifications_routes import notifications_bp

def register_blueprints(app):
    app.register_blueprint(login_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(set_notification_bp)
    app.register_blueprint(notifications_bp)
