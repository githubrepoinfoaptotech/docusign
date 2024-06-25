from models.Signature import Signature
from flask import make_response, jsonify, g
from database.db import db
from uuid import UUID


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
        return make_response({"message": "Error Happend", "status": False})


def edit_sign():
    pass
