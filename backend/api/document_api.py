from flask import Blueprint, g, request, make_response, jsonify
from utils.functions.upload import upload_file
from service import document_service
from utils.middlewares.auth import check_auth
from utils.functions.validation_models import validate_file_request, AddDocument
documentRoutes = Blueprint("documentRoutes", __name__)


@documentRoutes.post("/add")
@check_auth
@validate_file_request(AddDocument)
def add_document():
    files_data = upload_file(request)
    if files_data["error"]:
        return make_response(jsonify({"message": files_data["message"], "status": False}))
    else:
        data = files_data["data"]
        return document_service.add_document(data)

