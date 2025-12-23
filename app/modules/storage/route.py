from flask import Blueprint
from .controller import StorageController


storage_bp = Blueprint('storage', __name__)
storage_controller = StorageController()
@storage_bp.route('/public/<path:path>/<filename>', methods=['GET'])
def public(path, filename):
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
    result=storage_controller.public(path, filename)
    return result
      