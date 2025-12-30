from app.db.db import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    gold = db.Column(db.Integer, default=0)
    last_gift_claim = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    card_users = db.relationship('CardUser', backref='user', lazy=True, foreign_keys='CardUser.user_id')
    sales = db.relationship('CardMarket', backref='seller', lazy=True, foreign_keys='CardMarket.seller_id')
    purchases = db.relationship('CardMarket', backref='buyer', lazy=True, foreign_keys='CardMarket.buyer_id')

    def __repr__(self):
        return f'<User {self.username}>'