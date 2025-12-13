from app.db.db import db
from datetime import datetime


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