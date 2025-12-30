from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime, timedelta
import random

from app.db.models.user import User
from app.db.models.card import Card
from app.db.models.card_user import CardUser
from app.db.db import db


class Free_giftController:
    @jwt_required()
    def index(self):
        return {'message':'Free gift API is running'}, 200
    
    @jwt_required()
    def claim_gold(self):
        user_id = get_jwt_identity()
        user = User.query.filter_by(id=user_id).first()

        if not user:
            raise Exception("User Tidak ditemukan!")
        
        today = datetime.now()
        if user.last_gift_claim and (today - user.last_gift_claim) < timedelta(hours=5):
            raise Exception("Kamu sudah mengambil free gift hari ini")
        
        try:
            user.gold += 100
            user.last_gift_claim = today

            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise Exception("Failed to Update User: " + str(e))

        return f"Congrats! You got {100} gold"
    

    @jwt_required()
    def redeem_card(self):
        user_id = get_jwt_identity()
        user = User.query.get(user_id)

        if not user:
            raise Exception("User Tidak ditemukan!")

        today = datetime.now()
        if user.last_gift_claim and (today - user.last_gift_claim) < timedelta(hours=5):
            raise Exception("Kamu sudah mengambil free gift hari ini")

        cards = Card.query.all()
        random_card = random.randint(0, len(cards))
        card_star = random.randint(1, 5)

        user.last_claim = today

        cardUserNew = CardUser(user_id=user_id, card_id= cards[random_card].id, stars= card_star)
        db.session.add(cardUserNew)
        db.session.commit()

        try:
            user.last_gift_claim = today

            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise Exception("Failed to Update User: " + str(e))

        return {
            "status": True,
            "message": "Congrats! You got a new card",
            "card": {
                "card_id": random_card,
                "star": card_star
            }
        }, 200
