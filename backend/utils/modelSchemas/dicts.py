from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.User import User
from models.Signature import Signature


class UserDict(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True


class SignatureDict(SQLAlchemyAutoSchema):
    class Meta:
        model = Signature
        load_instance = True


class SignatureDictWithUser(SQLAlchemyAutoSchema):
    class Meta:
        model = Signature
        load_instance = True

    user = fields.Nested(UserDict())


class UserDictWithSign(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

    signature = fields.Nested(SignatureDict())

