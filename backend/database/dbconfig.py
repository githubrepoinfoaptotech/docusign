# config.py
import os
import dotenv
dotenv.load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("dbconnect")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
