from flask import Blueprint,request
from service import user_service
from utils.functions.validation_models import validate_request, Register, Login
userRoutes = Blueprint("userRoutes",__name__)


@userRoutes.post("/register")
@validate_request(Register)
def register():
    data = request.get_json()
    return user_service.register(data)


@userRoutes.post("/login")
@validate_request(Login)
def login():
    data = request.get_json()
    return user_service.login(data)

@userRoutes.post("/verify_user")
def verify_user():
    data = request.get_json()
    return user_service.verify_user(data)



