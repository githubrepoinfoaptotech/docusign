import datetime
import jwt
import os
import dotenv

dotenv.load_dotenv()

SECRET = os.getenv("JWT_SECRET")


def generate_token(payload):
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    # Add the 'exp' claim to the payload
    payload['exp'] = expiration_time
    # Encode the payload and create the JWT token
    token_body = jwt.encode(payload, SECRET, algorithm="HS256")
    # Construct the complete token
    token = "Bearer " + token_body
    return token


def verify_token(token):
    payload = jwt.decode(token, SECRET, algorithms=["HS256"])
    return payload
