from models.User import User
from flask import make_response, jsonify,render_template
from database.db import db
from werkzeug.security import check_password_hash
from utils.functions.jwt_functions import generate_token
from models.Document import Document
from uuid import UUID
from utils.functions import mailfunctions

def register(data):
    user = User.query.filter_by(username=data["username"]).first()
    print(user)
    if user:
        return make_response(jsonify({"message": "User Already Exists", "status": False}), 409)
    else:
        new_user = User(username=data["username"], password=data["password"], fullname=data["fullname"],
                        initial=data["initial"])
        db.session.add(new_user)
        db.session.commit()

        # adding to_id to documents if document sent to this new user
        db.session.query(Document).filter_by(to=data["username"]).update({"to_id": new_user.id})
        db.session.commit()
        mylink="https://infoaptotech.com"
        email_content = render_template(
                'email_verification_template.html',
                name=data["fullname"],
                sitename="Infoapto",
                link=mylink
            )
        html=email_content
        subject = "Registration Successfull!"
        to_address = data["username"]
        receiver_username = data["fullname"]
        # Send the email and store the response
        mailfunctions.send_verification_email(subject, html, to_address, receiver_username)
        return make_response(jsonify({"message": "User Created Successfully", "status": True}), 201)


def login(data):
    user_data = User.query.filter_by(username=data["username"]).first()
    if user_data:
        user = user_data.to_dict()
        if check_password_hash(user["password"], data["password"]):
            token = generate_token({"user_id": str(user["id"]), "name": user["fullname"]})
            return make_response(jsonify({"message": "Logged in", "token": token, "status": True}), 200)
        else:
            return make_response(jsonify({"message": "Password Missmatch", "status": False}), 423)
    else:
        return make_response(jsonify({"message": "User Not Exists Please Register", "status": False}), 406)

