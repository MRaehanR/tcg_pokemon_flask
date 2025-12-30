from flask import Flask
from flasgger import Swagger
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_seeder import FlaskSeeder
from app.db.db import db
from app.routes import routes
from app.db.models.user import User


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

        @jwt.user_identity_loader
        def user_identity_lookup(user_data):
            if isinstance(user_data, dict):
                return str(user_data.get("id")) 
            return str(user_data)

        @jwt.user_lookup_loader
        def user_lookup_callback(_jwt_header, jwt_data):
            identity = jwt_data["sub"] 
            return User.query.get(int(identity))

        return jwt

def initialize_seeder(app: Flask):
    with app.app_context():
        seeder = FlaskSeeder()
        seeder.init_app(app, db)
        return seeder
    
def initialize_cors(app: Flask):
    from flask_cors import CORS
    with app.app_context():
        CORS(app)