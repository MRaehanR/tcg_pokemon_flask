from flask import request
from app.db.models.card_market import CardMarket
from app.db.models.card_user import CardUser
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
            
            card_user = CardUser.query.filter_by(
                user_id=market.seller_id,
                card_id=market.card_id
            ).first()

            if not card_user:
                raise Exception("Data kartu penjual tidak ditemukan")

            card_user.user_id = user_id
            card_user.updated_at = datetime.utcnow()
            db.session.delete(market)
            db.session.commit()

            return {
                "message": "Pembelian berhasil",
                "market_id": market.id,
                "card_id": market.card_id,
                "pemilik_baru_id": user_id
            }

        except Exception as e:
            db.session.rollback()
            raise e
