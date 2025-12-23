from flask import request, jsonify
from app.db.models.card_market import CardMarket
from datetime import datetime
from app.utils.response import *
from app.db.db import db

class SellController:
    def index(self):
        seller_id = 1  

        data = request.get_json()
        if not data:
            return response_error("Invalid JSON body")

        card_id = data.get("card_id")
        price = data.get("price")

        if not card_id or price is None:
            return response_error("card_id and price are required")
        
        if price <= 0:
            return response_error("Price must be greater than zero")

        try:
            new_listing = CardMarket(
                card_id=card_id,
                seller_id=seller_id,
                price=price
            )

            db.session.add(new_listing)
            db.session.commit()
            
            return response_success({
                "id": new_listing.id,
                "card_id": new_listing.card_id,
                "price": new_listing.price
            })
            
        except Exception as e:
            db.session.rollback()
            return response_error(f"Database error: {str(e)}")
    
    def cancel(self):
        seller_id = 1 

        data = request.get_json()
        if not data:
            return response_error("Invalid JSON body")

        market_id = data.get("id")

        if not market_id:
            return response_error("Listing ID (id) is required")

        try:
            listing = CardMarket.query.filter_by(id=market_id, seller_id=seller_id).first()

            if not listing:
                return response_not_found("Listing not found or you don't have permission to cancel this.")

            db.session.delete(listing)
            db.session.commit()

            return response_success("Successfully canceled the sale.")

        except Exception as e:
            db.session.rollback()
            return response_error(f"Database error: {str(e)}")
