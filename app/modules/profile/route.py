from flask import Blueprint, make_response, jsonify
from .controller import ProfileController


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
    result=profile_controller.index()
    return make_response(jsonify(data=result))
      