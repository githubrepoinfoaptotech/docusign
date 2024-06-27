from flask import Blueprint, request
from service import sign_service
from utils.middlewares import auth
from utils.functions.validation_models import validate_request, AddSign
signRoutes = Blueprint("signRoutes",__name__)


@signRoutes.post("/add")
@auth.check_auth
@validate_request(AddSign)
def add_sign():
    data = request.get_json()
    return sign_service.add_sign(data)


@signRoutes.get("/getSign")
@auth.check_auth
def get_sign():
    return sign_service.get_sign()

