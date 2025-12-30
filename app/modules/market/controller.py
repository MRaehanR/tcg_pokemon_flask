from flask import request, jsonify
from flask_jwt_extended import jwt_required, current_user
from app.db.models.card_market import CardMarket
from app.db.models.card_user import CardUser
from app.db.models.card import Card

class MarketController:
    @jwt_required()
    def market(self):
        user_id = current_user.id

        param_user_id = request.args.get("user_id", None)
        search = request.args.get("search", None)
        sort_price = request.args.get("price", None)

        query = CardMarket.query.join(CardMarket.card_user).join(CardUser.card)

        if param_user_id:
            query = query.filter(CardMarket.seller_id == param_user_id)

        if search:
            query = query.filter(CardUser.card.has(Card.name.like(f"%{search}%")))

        if sort_price == "asc":
            query = query.order_by(CardMarket.price.asc())
        elif sort_price == "desc":
            query = query.order_by(CardMarket.price.desc())
        else:
            query = query.order_by(CardMarket.created_at.desc())

        markets = query.all()

        market_data = []
        for m in markets:
            market_data.append({
                "market_id": m.id,
                "card_id": m.card_user.card.id if m.card_user and m.card_user.card else None,
                "card_name": m.card_user.card.name if m.card_user and m.card_user.card else None,
                "image": m.card_user.card.image_path if m.card_user and m.card_user.card else None,
                "stars": m.card_user.stars if m.card_user else None,
                "price": m.price,
                "tanggal_jual": str(m.created_at),
                "seller_id": m.seller_id
            })

        return {
            "user_id": user_id,
            "market": market_data
        }
