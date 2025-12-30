from flask_seeder import Seeder, Faker, generator
from app.db.models.card_market import CardMarket
from app.db.models.card_user import CardUser
from random import randint

class CardMarketSeeder(Seeder):
    def __init__(self):
        self.priority = 4
        
    def run(self):
        cardUser1 = CardUser.query.filter_by(user_id=11).all()
        
        # Get only first 5 cards from user 11
        for card_user in cardUser1[:5]:
            cardUserSells = CardMarket(
                seller_id=11,
                card_id=card_user.id,
                price=randint(10, 1000)
            )
            self.db.session.add(cardUserSells)