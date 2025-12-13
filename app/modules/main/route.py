from flask import Blueprint
from .controller import MainController
from flask_jwt_extended import jwt_required
from app.utils.response import response_success


main_bp = Blueprint('main', __name__)
main_controller = MainController()
@main_bp.route('/', methods=['GET'])
@jwt_required()
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
    result=main_controller.index()
    return response_success(result)
      