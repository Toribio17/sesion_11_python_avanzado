from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.services.status.status import Status

status_blueprint = Blueprint("status", __name__, url_prefix="/status")


@status_blueprint.route("/", methods=["GET", "POST"])
def hello():
    return "Hello, this is OCR Status API"