from flask import Blueprint, make_response, jsonify
from app.utils.response import response_success, response_error
from .controller import AuthController


auth_bp = Blueprint('auth', __name__)
auth_controller = AuthController()

@auth_bp.route('/login', methods=['POST'])
def login():
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
        result=auth_controller.login()
    except Exception as e:
        return response_error(str(e), status_code=401)
    return response_success(result)


@auth_bp.route('/register', methods=['POST'])
def register():
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
        result=auth_controller.register()
    except Exception as e:
        return response_error(str(e), status_code=401)
    return response_success(result)