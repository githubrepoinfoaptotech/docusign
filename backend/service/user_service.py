from models.User import User
from flask import make_response, jsonify,render_template
from database.db import db
from werkzeug.security import check_password_hash
from utils.functions.jwt_functions import generate_token
from models.Document import Document
from uuid import UUID
from utils.functions import mailfunctions

import random

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
        otp=generate_otp()
        # adding to_id to documents if document sent to this new user
        db.session.query(Document).filter_by(to=data["username"]).update({"to_id": new_user.id,"otp":otp,"verifyId":new_user.id})
        db.session.commit()
        verifyid=str(new_user.id)
        mylink="https://infoaptotech.com"
        email_content = render_template(
                'email_verification_template.html',
                name=data["fullname"],
                sitename="Infoapto",
                link=mylink,
                otp=otp
            )
        html = email_content
        subject = "Registration Successfull!"
        to_address = data["username"]
        receiver_username = data["fullname"]
        # Send the email and store the response
        mailfunctions.send_verification_email(subject, html, to_address, receiver_username)
        return make_response(jsonify({"message": "User Created Successfully", "status": True, "verificationId":verifyid}), 201)


def login(data):
    user_data = User.query.filter_by(username=data["username"]).first()
    if user_data:
        user = user_data.to_dict()
        if(user['isVerified']==True):
            if check_password_hash(user["password"], data["password"]):
                token = generate_token({"user_id": str(user["id"]), "name": user["fullname"]})
                return make_response(jsonify({"message": "Logged in", "token": token, "status": True}), 200)
            else:
                return make_response(jsonify({"message": "Password Missmatch", "status": False}), 423)
        else:
            return make_response(jsonify({"message": "Email Not Verified", "status": False}), 500)
    else:
        return make_response(jsonify({"message": "User Not Exists Please Register", "status": False}), 406)

def verify_user(data):
    user_data = User.query.filter_by(verifyId=data["token"]).first()
    if user_data:
        user = user_data.to_dict()
        if user['otp']==data["otp"]:
            user_data.verifyId=None
            user_data.isVerified=True
            user_data.otp=None
            db.session.commit()
            return make_response(jsonify({"message": "Success","status": True}), 200)
        else:
            return make_response(jsonify({"message": "Invalid Otp", "status": False}), 406)
    else:
        return make_response(jsonify({"message": "Invalid Action", "status": False}), 406)
def edit_user(data):
    user_data = User.query.filter_by(id=UUID(data["user_id"])).first()
    if user_data:  
        user_data.fullname=data['fullname']
        user_data.initial=data['initial']
        db.session.commit()
        return make_response(jsonify({"message": "User Updated","status": True}), 200)
    else:
        return make_response(jsonify({"message": "User Not Exists Please Register", "status": False}), 406)

def generate_otp(length=6):
    """Generate a numeric OTP of a specified length."""
    if length <= 0:
        raise ValueError("OTP length must be a positive integer")
    otp = ''.join(random.choices('0123456789', k=length))
    return otp