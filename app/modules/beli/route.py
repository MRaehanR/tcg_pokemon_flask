from flask import Blueprint, make_response, jsonify
from app.utils.response import response_success, response_error
from .controller import BeliController


beli_bp = Blueprint('beli', __name__)
beli_controller = BeliController()

@beli_bp.route('/post', methods=['POST'])
def beli():
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
        result=beli_controller.beli()
    except Exception as e:
        return response_error(str(e), status_code=401)
    return response_success(result)
      