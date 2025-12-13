from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    gold = db.Column(db.Integer, default=0)
    last_gift_claim = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    card_users = db.relationship('CardUsers', backref='user', lazy=True, foreign_keys='CardUsers.user_id')
    sales = db.relationship('CardMarket', backref='seller', lazy=True, foreign_keys='CardMarket.seller_id')
    purchases = db.relationship('CardMarket', backref='buyer', lazy=True, foreign_keys='CardMarket.buyer_id')

    def __repr__(self):
        return f'<User {self.username}>'


class Cards(db.Model):
    __tablename__ = 'cards'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    spread = db.Column(db.Integer, nullable=False)
    max_spread = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    card_users = db.relationship('CardUsers', backref='card', lazy=True)

    def __repr__(self):
        return f'<Card {self.name}>'


class CardUsers(db.Model):
    __tablename__ = 'card_users'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    card_id = db.Column(db.Integer, db.ForeignKey('cards.id'), nullable=False)
    stars = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    card_market = db.relationship('CardMarket', backref='card_user', lazy=True)

    def __repr__(self):
        return f'<CardUser user_id={self.user_id} card_id={self.card_id}>'


class CardMarket(db.Model):
    __tablename__ = 'card_market'
    
    id = db.Column(db.Integer, primary_key=True)
    card_id = db.Column(db.Integer, db.ForeignKey('card_users.card_id'), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    buyer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    price = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<CardMarket id={self.id} price={self.price}>'