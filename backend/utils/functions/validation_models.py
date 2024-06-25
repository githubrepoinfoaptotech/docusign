from pydantic import BaseModel, EmailStr, field_validator, ValidationError, model_validator
from flask import request, jsonify
from functools import wraps
from werkzeug.datastructures import FileStorage
import json


def validate_request(model):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                data = request.json
                model(**data)
                return f(*args, **kwargs)
            except ValidationError as e:
                response = jsonify({"error": e.errors()})
                response.status_code = 400
                return response
        return decorated_function
    return decorator


def validate_file_request(model):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                data = {**request.form.to_dict(), **request.files.to_dict()}
                model(**data)
                return f(*args, **kwargs)
            except ValidationError as e:
                error_messages = []
                for error in e.errors():
                    error_messages.append(f"{error['loc']}: {error['msg']}")
                return jsonify({"error": True, "message": error_messages}), 400
            except ValueError as ve:
                return jsonify({"error": True, "message": str(ve)}), 400
        return decorated_function
    return decorator


class Register(BaseModel):
    username: EmailStr
    password: str
    fullname: str
    initial: str

    @field_validator("initial")
    @classmethod
    def initial_check(cls, value: str):
        if len(value) == 2 or len(value) == 1:
            return value
        else:
            raise ValueError('"Initial" String Must be 1 or 2 letters.')


class Login(BaseModel):
    username: EmailStr
    password: str


class AddStatus(BaseModel):
    status: str


class AddSign(BaseModel):
    font_name: str
    signature_name: str
    initial_name: str

    @field_validator("initial_name")
    @classmethod
    def initial_check(cls, value: str):
        if len(value) == 2 or len(value) == 1:
            return value
        else:
            raise ValueError('"Initial" String Must be 1 or 2 letters.')


class Coordinate(BaseModel):
    x: float
    y: float
    scale: float


class AddDocument(BaseModel):
    file: FileStorage
    sign_coordinates: str
    initial_coordinates: str
    to: EmailStr

    class Config:
        arbitrary_types_allowed = True

    @model_validator(mode="before")
    @classmethod
    def coordinates_check(cls, values: dict):
        try:
            sign_data = json.loads(values.get("sign_coordinates", '[]'))
            initial_data = json.loads(values.get("initial_coordinates", '[]'))
            for coord in sign_data:
                try:
                    Coordinate(**coord)
                except ValidationError as e:
                    raise ValueError(f"Invalid Sign coordinate data: {e}")

            for coord in initial_data:
                try:
                    Coordinate(**coord)
                except ValidationError as e:
                    raise ValueError(f"Invalid initial coordinate data: {e}")
        except json.JSONDecodeError as e:
            response = jsonify({"error": e.msg})
            response.status_code = 400
            return response
        except ValidationError as e:
            raise ValueError(f"Invalid JSON format: {e}")

        return values
