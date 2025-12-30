from flask_seeder import Seeder, Faker, generator
from app.db.models.card_user import CardUser

class CardUserSeeder(Seeder):
    def __init__(self):
        self.priority = 3
        
    def run(self):
        faker = Faker(cls=CardUser, init={
            'user_id': generator.Integer(1, 10),
            'card_id': generator.Integer(1, 10),
            'stars': generator.Integer(0, 5),
        })
        
        for card_user in faker.create(30):
            self.db.session.add(card_user)
            
        user1 = Faker(cls=CardUser, init={
            'user_id': 11,
            'card_id': generator.Integer(1, 10),
            'stars': generator.Integer(1, 5),
        })
        for card_user in user1.create(10):
            self.db.session.add(card_user)