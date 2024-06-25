from flask import Blueprint, request
from service import status_service
from utils.middlewares.auth import check_auth
from utils.functions.validation_models import validate_request, AddStatus
statusRoutes = Blueprint("statusRoutes", __name__)


@statusRoutes.post("/add")
@check_auth
@validate_request(AddStatus)
def add_status():
    data = request.get_json()
    return status_service.add_status(data)

