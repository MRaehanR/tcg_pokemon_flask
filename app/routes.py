from flask import Flask
from app.modules.main.route import main_bp

def routes(app: Flask):
    app.register_blueprint(main_bp, url_prefix='/api/v1/main')