from models.Signature import Signature
from models.User import User
from flask import make_response, jsonify, g
from database.db import db
from uuid import UUID
from utils.modelSchemas.dicts import SignatureDictWithUser, SignatureDict
from sqlalchemy import select
from sqlalchemy.orm import session


def add_sign(data):
    try:
        sign = Signature.query.filter_by(user_id=UUID(data["user_id"])).first()
        if sign:
            return make_response(jsonify({"message": "Already Sign Exists", "status": False}), 302)
        else:
            newsign = Signature(font_name=data["font_name"], signature_name=data["signature_name"],
                                initial_name=data["initial_name"], user_id=UUID(g.local_data.get("user_id")))
            db.session.add(newsign)
            db.session.commit()
            return make_response(jsonify({"message": "Signature Added", "status": True}), 201)

    except Exception as e:
        print(e)
        return make_response(jsonify({"message": "Error Happend", "status": False}))


def edit_sign():
    pass


def get_sign():
    try:
        # select_stmt = (select(Signature, User.fullname, User.id, User.initial, User.createdAt).join(User)
        #                .where(Signature.user_id == UUID(g.local_data.get("user_id"))).limit(1))
        # sign = (Signature.query
        #         # .with_entities(Signature.id, Signature.signature_name, Signature.initial_name)
        #         .filter_by(user_id=UUID(g.local_data.get("user_id"))).join(User).first())
        sign = Signature.query.where(Signature.user_id == UUID(g.local_data.get("user_id"))).first()
        # sign = db.session.execute(select_qr).scalars()
        if sign:
            signature_schema = SignatureDictWithUser()
            # print(sign.__dict__)
            sign_data = signature_schema.dump(sign)
            return make_response(jsonify({"data": sign_data, "status": True}), 200)
        else:
            return make_response(jsonify({"message": "sign Not found", "status": False}), 100)
    except Exception as e:
        print(e)
        return make_response(jsonify({"message": "Error Happend", "status": False}), 500)
