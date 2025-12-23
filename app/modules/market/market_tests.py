import unittest
import json

from app.modules.market.controller import MarketController


def test_index():
    market_controller = MarketController()
    result = market_controller.index()
    assert result == {'message': 'Hello, World!'}
