from flask import request
from app import app
from app.db.models.market import Market
from app.db.db import db

class MarketController:
    def market(self):
        user_id = request.json.get("user_id", None)
        search = request.json.get("search", None)
        price = request.json.get("price", None)
        query = Market.query
        if user_id:
            query = query.filter_by(user_id=user_id)
        if search:
            query = query.filter(Market.name.like(f"%{search}%"))
        if price == "asc":
            query = query.order_by(Market.price.asc())
        elif price == "desc":
            query = query.order_by(Market.price.desc())
        markets = query.all()

        data = []
        for m in markets:
            data.append({
                "id": m.id,
                "name": m.name,
                "price": m.price,
                "stock": m.stock,
                "user_id": m.user_id
            })
        return data
market = MarketController()

@app.route("/api/v1/market", methods=["POST"])
def market_index():
    return market.market()
