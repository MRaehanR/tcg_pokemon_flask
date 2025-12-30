from flask import request
from flask_jwt_extended import jwt_required, current_user
from app.db.models.user import User
from app.db.models.card_user import CardUser

class ProfileController:
    @jwt_required()
    def index(self):
        user_id = current_user.id

        is_sell_mode = request.args.get('sell') == 'true'

        user = User.query.filter_by(id=user_id).first()
        if not user:
            raise Exception("User not found")

        card_users = CardUser.query.filter_by(user_id=user_id).all()

        user_cards = []
        for cu in card_users:
            is_in_market = True if cu.card_market else False
            
            if is_sell_mode and is_in_market:
                continue

            user_cards.append({
                "card_user_id": cu.id,
                "card_id": cu.card.id,
                "card_name": cu.card.name,         
                "stars": cu.stars,
                "spread": cu.card.spread,
                "max_spread": cu.card.max_spread,
                "image": cu.card.image_path,
                "is_in_market": is_in_market
            })

        return {
            "user": {
                "id": user.id,
                "username": user.username,
                "gold": user.gold
            },
            "cards": user_cards
        }
