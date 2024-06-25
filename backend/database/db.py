from flask_sqlalchemy import SQLAlchemy
from contextlib import contextmanager
from sqlalchemy.exc import OperationalError


db = SQLAlchemy()
