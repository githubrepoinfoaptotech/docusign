from functools import wraps
from flask import request, make_response, g
from utils.functions.jwt_functions import verify_token
from jwt.exceptions import ExpiredSignatureError


def check_auth(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        authorization = request.headers.get("authorization")
        if authorization:
            token = authorization.split(" ")[1]
            try:
                payload = verify_token(token)
            except ExpiredSignatureError:
                return make_response({"message": "Token Expired", "status": False}, 401)
            if payload:
                g.local_data = payload
                return func(*args, **kwargs)
            else:
                return make_response({"message": "UnAuthorized", "status": False}, 401)
        else:
            return make_response({"message": "UnAuthorized", "status": False}, 401)

    return decorated_function
