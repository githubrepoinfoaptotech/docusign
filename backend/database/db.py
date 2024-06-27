from flask_sqlalchemy import SQLAlchemy
from contextlib import contextmanager
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
