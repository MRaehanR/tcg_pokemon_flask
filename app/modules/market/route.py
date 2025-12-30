from flask import Blueprint, make_response, jsonify
from app.utils.response import response_success, response_error
from .controller import MarketController


market_bp = Blueprint('market', __name__)
market_controller = MarketController()
@market_bp.route('/get', methods=['GET'])
def market_route():
    """ Example endpoint with simple greeting.
    ---
    tags:
      - Example API
    responses:
      200:
        description: A simple greeting
        schema:
          type: object
          properties:
            data:
              type: object
              properties:
                message:
                  type: string
                  example: "Hello World!"
    """
    result=market_controller.market()
    return make_response(jsonify(data=result))
      