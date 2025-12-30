from flask import request
from app.db.models.card_market import CardMarket
from app.db.models.card_user import CardUser
from app.db.models.user import User
from flask_jwt_extended import jwt_required, current_user
from datetime import datetime
from app.db.db import db


class BeliController:
    @jwt_required()
    def beli(self):
        user_id = current_user.id
        market_id = request.json.get("id")

        if not market_id:
            raise Exception("ID harus diisi")

        try:
            market = CardMarket.query.filter_by(id=market_id).first()
            if not market:
                raise Exception("Produk tidak ditemukan")

            if market.seller_id == user_id:
                raise Exception("Tidak bisa membeli kartu sendiri")
            
            # Get buyer data
            buyer = User.query.filter_by(id=user_id).first()
            if not buyer:
                raise Exception("User tidak ditemukan")
            
            # Check if buyer has enough gold
            if buyer.gold < market.price:
                raise Exception(f"Gold tidak cukup. Anda memiliki {buyer.gold} gold, harga kartu {market.price} gold")
            
            # Get seller data
            seller = User.query.filter_by(id=market.seller_id).first()
            if not seller:
                raise Exception("Penjual tidak ditemukan")
            
            card_user = CardUser.query.filter_by(
                user_id=market.seller_id,
                id=market.card_id
            ).first()

            if not card_user:
                raise Exception("Data kartu penjual tidak ditemukan")

            # Deduct buyer's gold
            buyer.gold -= market.price
            buyer.updated_at = datetime.utcnow()
            
            # Add gold to seller
            seller.gold += market.price
            seller.updated_at = datetime.utcnow()
            
            # Transfer card ownership
            card_user.user_id = user_id
            card_user.updated_at = datetime.utcnow()
            
            # Delete market entry
            db.session.delete(market)
            db.session.commit()

            return {
                "message": "Pembelian berhasil",
                "market_id": market.id,
                "card_id": market.card_id,
                "price": market.price,
                "pemilik_baru_id": user_id,
                "gold_tersisa": buyer.gold
            }

        except Exception as e:
            db.session.rollback()
            raise e
