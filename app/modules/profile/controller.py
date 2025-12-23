from flask_jwt_extended import jwt_required, current_user
from app.db.models.user import User
from app.db.models.card_user import CardUser

class ProfileController:
    @jwt_required()
    def index(self):
        user_id = current_user.id

        user = User.query.filter_by(id=user_id).first()
        if not user:
            raise Exception("User not found")

        card_users = CardUser.query.filter_by(user_id=user_id).all()

        user_cards = []
        for cu in card_users:
            user_cards.append({
                "card_user_id": cu.id,
                "card_id": cu.card.id,
                "card_name": cu.card.name,         
                "stars": cu.stars,
                "spread": cu.card.spread,
                "max_spread": cu.card.max_spread,
                "image": cu.card.image_path
            })

        return {
            "user": {
                "id": user.id,
                "username": user.username,
                "gold": user.gold
            },
            "cards": user_cards
        }
