from flask import make_response, jsonify

def response_success(data, status_code=200):
    response = {
        "code": status_code,
        "message": "Success",
        "data": data
    }
    return make_response(jsonify(response), status_code)

def response_error(message, status_code=400):
    response = {
        "code": status_code,
        "message": message,
        "data": None
    }
    return make_response(jsonify(response), status_code)

def response_not_found(message="Resource not found", status_code=404):
    response = {
        "code": status_code,
        "message": message,
        "data": None
    }
    return make_response(jsonify(response), status_code)