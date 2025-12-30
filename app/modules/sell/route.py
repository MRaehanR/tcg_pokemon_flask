from flask import Blueprint, make_response, jsonify
from .controller import SellController
from app.utils.response import response_success


sell_bp = Blueprint('sell', __name__)
sell_controller = SellController()
@sell_bp.route('/post', methods=['POST'])
def index():
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
    result=sell_controller.index()
    return result

@sell_bp.route('/cancel', methods=['DELETE'])
def cancel_sale():
    """ Cancel a card sale listing
    ---
    tags:
      - Sell API
    parameters:
      - in: body
        name: body
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
    responses:
      200:
        description: Sale canceled successfully
    """
    return sell_controller.cancel()

      