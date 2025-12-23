from flask_seeder import Seeder, Faker, generator
from app.db.models.card import Card

class CardSeeder(Seeder):
    def run(self):
        pokemon_names = ['charizard', 'gengar', 'gyarados', 'moltres', 'pidgeotto', 'pikachu', 'rapidash', 'snorlax', 'venusaur', 'weepinbell']
        
        # Charizard cards
        for index in range(5):
            self.db.session.add(Card(
                name=pokemon_names[0],
                spread=0,
                max_spread=10,
                image_path=f'/storage/public/images/cards/{pokemon_names[0]}.png'
            ))

        # Gengar cards
        for index in range(5):
            self.db.session.add(Card(
                name=pokemon_names[1],
                spread=0,
                max_spread=15,
                image_path=f'/storage/public/images/cards/{pokemon_names[1]}.png'
            ))
        
        # Gyarados cards
        for index in range(5):
            self.db.session.add(Card(
                name=pokemon_names[2],
                spread=0,
                max_spread=12,
                image_path=f'/storage/public/images/cards/{pokemon_names[2]}.png'
            ))
        
        # Moltres cards
        for index in range(5):
            self.db.session.add(Card(
                name=pokemon_names[3],
                spread=0,
                max_spread=8,
                image_path=f'/storage/public/images/cards/{pokemon_names[3]}.png'
            ))
        
        # Pidgeotto cards
        for index in range(5):
            self.db.session.add(Card(
                name=pokemon_names[4],
                spread=0,
                max_spread=20,
                image_path=f'/storage/public/images/cards/{pokemon_names[4]}.png'
            ))
        
        # Pikachu cards
        for index in range(5):
            self.db.session.add(Card(
                name=pokemon_names[5],
                spread=0,
                max_spread=25,
                image_path=f'/storage/public/images/cards/{pokemon_names[5]}.png'
            ))
        
        # Rapidash cards
        for index in range(5):
            self.db.session.add(Card(
                name=pokemon_names[6],
                spread=0,
                max_spread=14,
                image_path=f'/storage/public/images/cards/{pokemon_names[6]}.png'
            ))
        
        # Snorlax cards
        for index in range(5):
            self.db.session.add(Card(
                name=pokemon_names[7],
                spread=0,
                max_spread=18,
                image_path=f'/storage/public/images/cards/{pokemon_names[7]}.png'
            ))
        
        # Venusaur cards
        for index in range(5):
            self.db.session.add(Card(
                name=pokemon_names[8],
                spread=0,
                max_spread=11,
                image_path=f'/storage/public/images/cards/{pokemon_names[8]}.png'
            ))
        
        # Weepinbell cards
        for index in range(5):
            self.db.session.add(Card(
                name=pokemon_names[9],
                spread=0,
                max_spread=22,
                image_path=f'/storage/public/images/cards/{pokemon_names[9]}.png'
            ))
            
        
            
        
        
            
            