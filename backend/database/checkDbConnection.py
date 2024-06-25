from sqlalchemy.exc import OperationalError
from sqlalchemy import text


def check_db_connection(database):
    try:
        # Attempt to execute a simple query
        database.session.execute(text('SELECT 1'))
    except OperationalError:
        # If an OperationalError occurs, roll back the session
        database.session.rollback()

