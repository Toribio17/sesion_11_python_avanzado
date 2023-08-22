from flask import Blueprint
from app.services.ocr.ocr import Ocr_Process
from flask_jwt_extended import jwt_required


ocr_blueprint = Blueprint("ocr", __name__, url_prefix="/ocr")

#process a single file
@ocr_blueprint.route("/ocrOneFile/<document_name>", methods=["GET", "POST"])
@jwt_required()
def ocr_single_file(document_name):
    obj_ocr = Ocr_Process()
    obj_ocr.optical_character_recognition(document_name)
    return "ocr single file: " + str(document_name)

