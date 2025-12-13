from app.db.db import db
from datetime import datetime


class CardUser(db.Model):
    __tablename__ = 'card_users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    card_id = db.Column(db.Integer, db.ForeignKey('cards.id'), nullable=False)
    stars = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    card_market = db.relationship('CardMarket', backref='card_user', lazy=True)

    def __repr__(self):
        return f'<CardUser user_id={self.user_id} card_id={self.card_id}>'