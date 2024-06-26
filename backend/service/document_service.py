from flask import make_response, jsonify, g
from models.Document import Document
from models.User import User
from database.db import db
from uuid import UUID
import json


def add_document(data):
    print(data)
    try:
        parsed_sign_data = json.loads(data["initial_coordinates"])
        parsed_initial_data = json.loads(data["sign_coordinates"])
        if (len(parsed_sign_data) != 0) or (len(parsed_initial_data) != 0):

            save_data = {"document": data["filename"], "user_id": UUID(g.local_data.get("user_id")),
                        "sign_coordinates": data["sign_coordinates"],
                        "initial_coordinates": data["initial_coordinates"], "to": data["to"]}

            user_data = User.query.filter_by(username=data["to"]).first()
            if user_data:
                user = user_data.to_dict()
                save_data["to_id"] = user["id"]

            new_document = Document(**save_data)
            db.session.add(new_document)
            db.session.commit()
            return make_response(jsonify({"message": "Document Saved Successfully", "status": True}), 201)
        else:
            return make_response(jsonify({"message": "Choose One Signature or Initial Signature",
                                        "status": False}), 406)
    except Exception as e:
        print(e)
        return make_response(jsonify({"message": "Invalid Action", "status": False}),500)

def send_document(data):
    try:
        link="https://infoaptotech.com"
        email=data['email']
        
    except Exception as e:
        print(e)
        return make_response(jsonify({"message": "Invalid Action", "status": False}),500)

