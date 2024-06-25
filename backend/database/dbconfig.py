# config.py
import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://nsai_user:helloworld@localhost/docusign'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
