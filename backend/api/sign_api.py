from flask import Blueprint, request
from service import sign_service
from utils.middlewares import auth
from utils.functions.validation_models import validate_request, AddSign,EditSign
signRoutes = Blueprint("signRoutes",__name__)


@signRoutes.post("/add")
@auth.check_auth
@validate_request(AddSign)
def add_sign():
    data = request.get_json()
    return sign_service.add_sign(data)

@signRoutes.post("/edit")
@auth.check_auth
@validate_request(EditSign)
def edit_sign():
    data = request.get_json()
    return sign_service.edit_sign(data)