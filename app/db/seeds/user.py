from flask_seeder import Seeder, Faker, generator
from app.db.models.user import User
from werkzeug.security import generate_password_hash

class UserSeeder(Seeder):
    def run(self):
        faker = Faker(cls=User, init={
            'username': generator.Name(),
            'password': generate_password_hash('password123'),
            'gold': generator.Integer(100, 1000),
        })
        
        for user in faker.create(10):
            self.db.session.add(user)
            
        user1 = User(
            username='user1',
            password=generate_password_hash('password'),
            gold=500
        )
        self.db.session.add(user1)