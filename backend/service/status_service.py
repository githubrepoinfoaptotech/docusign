from models.DocumentStatus import DocumentStatus
from flask import make_response, g, jsonify
from database.db import db


def add_status(data):
    status = DocumentStatus.query.filter(DocumentStatus.status.ilike(f"{data['status']}")).first()
    if status:
        print(g.local_data)
        return make_response(jsonify({"message": "Status Already Exists", "status": False}), 302)
    else:
        new_status = DocumentStatus(status=data["status"])
        db.session.add(new_status)
        db.session.commit()
        return make_response(jsonify({"message": "Status Created Successfully", "status": True}), 201)


