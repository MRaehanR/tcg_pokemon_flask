from flask import Blueprint, make_response, jsonify
from .controller import Free_giftController
from app.utils.response import response_success, response_error



free_gift_bp = Blueprint('free_gift', __name__)
free_gift_controller = Free_giftController()
@free_gift_bp.route('/free', methods=['GET'])
def claim_gold():
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
    try:
        result=free_gift_controller.claim_gold()
    except Exception as e:
        return response_error(str(e), status_code=400)
    return response_success(message=result)
      
@free_gift_bp.route('/reedem_card', methods=['GET'])
def reedem_card():
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
    try:
        result=free_gift_controller.redeem_card()
    except Exception as e:
        return response_error(str(e), status_code=400)
    return response_success(result)