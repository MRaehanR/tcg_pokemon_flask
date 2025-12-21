from flask import Flask
from app.modules.main.route import main_bp
from app.modules.auth.route import auth_bp
from app.modules.profile.route import market_bp
from app.modules.profile.route import profile_bp

def routes(app: Flask):
    app.register_blueprint(main_bp, url_prefix='/api/v1/main')
    app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')
    app.register_blueprint(profile_bp, url_prefix='/api/v1/market')
    app.register_blueprint(profile_bp, url_prefix='/api/v1/profile')
