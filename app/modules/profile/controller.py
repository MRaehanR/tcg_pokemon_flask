from flask import request
from app.db.models.user import User

class ProfileController:
    def profile(self):
        username = request.json.get("username", None)
        
        user = User.query.filter_by(username=username).first()
        if not user:
            raise Exception("User not found")

        return {
            "id": user.id,
            "username": user.username,
            "nama": user.nama,
            "gold": user.gold,
            "exp": user.exp,
            "level": user.level
        }