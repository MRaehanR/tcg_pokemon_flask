from flask import Blueprint, make_response, jsonify
from .controller import ProfileController
from app.utils.response import response_success, response_error


profile_bp = Blueprint('profile', __name__)
profile_controller = ProfileController()
@profile_bp.route('/', methods=['GET'])
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
    try:
        result=profile_controller.index()
    except Exception as e:
        return response_error(str(e), status_code=401)
    return response_success(result)
      