from flask import Request, jsonify
from werkzeug.utils import secure_filename
from os import path
from datetime import datetime
from random import shuffle

# Allowed extensions for files
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'doc', 'docx'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_file(req: Request):
    if 'file' not in req.files:
        return {"error": True, "message": "Files not given", "status": False}
    file = req.files['file']
    if file.filename == '':
        return {"error": True, "message": "No selected file", "status": False}
    if allowed_file(file.filename):
        filename_1 = secure_filename(file.filename)
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        time_list = list(timestamp)
        shuffle(time_list)
        timestamp = "".join(time_list)
        # D:\python\docusign_project\backend\utils
        upload_folder = path.abspath(path.join(path.dirname(__file__), "../uploads"))
        filename = path.join(upload_folder, f"{timestamp}_{filename_1}")
        file.save(filename)
        form_data = {}
        for key in req.form:
            form_data[key] = req.form[key]

        # Convert form data to JSON
        form_data_json = dict(form_data)
        form_data_json["filename"] = filename
        return {"error": False, "message": "File successfully uploaded", "filename": filename,
                "data": form_data_json, "status": True}

    else:
        return {"error": True, "message": "File Ext Not allowed", "status": False}

