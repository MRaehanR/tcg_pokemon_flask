from flask import Flask
from app.modules.main.route import main_bp
from app.modules.auth.route import auth_bp
from app.modules.market.route import market_bp
from app.modules.profile.route import profile_bp
from app.modules.sell.route import sell_bp
from app.modules.storage.route import storage_bp
from app.modules.beli.route import beli_bp

def routes(app: Flask):
    app.register_blueprint(main_bp, url_prefix='/api/v1/main')
    app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')
    app.register_blueprint(market_bp, url_prefix='/api/v1/market')
    app.register_blueprint(profile_bp, url_prefix='/api/v1/profile')
    app.register_blueprint(sell_bp, url_prefix='/api/v1/sell')
    app.register_blueprint(storage_bp, url_prefix='/storage')
    app.register_blueprint(beli_bp, url_prefix='/api/v1/beli')
