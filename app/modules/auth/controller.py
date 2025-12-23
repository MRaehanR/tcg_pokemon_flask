from flask_jwt_extended import create_access_token
from flask import request
from app.db.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from app.db.db import db

class AuthController:
    def login(self):
        username = request.json.get("username", None)
        password = request.json.get("password", None)
        
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            raise Exception("Bad username or password")
        
        identityUser = {
            "id": user.id,
            "username": user.username
        }

        access_token = create_access_token(identity=identityUser)
        return {"access_token": access_token}
    
    def register(self):
        username = request.json.get("username", None)
        password = request.json.get("password", None)
        
        if not username or not password:
            raise Exception("Username and password are required")
        
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            raise Exception("Username already exists")
        
        hashed_password = generate_password_hash(password)
        
        try:
            new_user = User(username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise Exception("Failed to create user: " + str(e))
        
        identityUser = {
            "id": new_user.id,
            "username": new_user.username
        }
        
        access_token = create_access_token(identity=identityUser)
        return {"access_token": access_token}