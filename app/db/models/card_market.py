from app.db.db import db
from datetime import datetime


class CardMarket(db.Model):
    __tablename__ = 'card_market'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    card_id = db.Column(db.Integer, db.ForeignKey('card_users.card_id'), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    buyer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    price = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<CardMarket id={self.id} price={self.price}>'