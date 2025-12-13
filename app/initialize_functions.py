from flask import Flask
from flasgger import Swagger
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from app.db.db import db
from app.routes import routes


def initialize_route(app: Flask):
    with app.app_context():
        routes(app)


def initialize_db(app: Flask):
    with app.app_context():
        db.init_app(app)
        # db.create_all()
        migrate = Migrate(app, db, directory='app/db/migrations')
        return db, migrate
def initialize_swagger(app: Flask):
    with app.app_context():
        swagger = Swagger(app)
        return swagger
    
def initialize_jwt(app: Flask):
    with app.app_context():
        jwt = JWTManager(app)
        return jwt