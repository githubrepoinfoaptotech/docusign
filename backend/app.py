from flask import Flask
from database import dbconfig
from database.db import db
from database.checkDbConnection import check_db_connection
from api import user_api, sign_api, status_api, document_api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config.from_object(dbconfig.Config)
db.init_app(app)


@app.before_request
def before_request():
    check_db_connection(db)


@app.get("/")
def hello():
    return {"message": "Hello World", "status": True}


app.register_blueprint(user_api.userRoutes, url_prefix="/api/user")
app.register_blueprint(sign_api.signRoutes, url_prefix="/api/sign")
app.register_blueprint(status_api.statusRoutes, url_prefix="/api/status")
app.register_blueprint(document_api.documentRoutes, url_prefix="/api/document")


with app.app_context():
    from models.User import User
    from models.Signature import Signature
    from models.DocumentStatus import DocumentStatus
    from models.Document import Document
    db.create_all()
    db.session.commit()




# Remove the if __name__ == '__main__' block
if __name__ == '__main__':
    app.run(debug=True, port=8080)