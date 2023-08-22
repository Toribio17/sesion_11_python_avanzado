from flask import Blueprint
from app.services.object_storage.object_storage import ObjectStorageServices as cos
from flask_jwt_extended import jwt_required


cos_blueprint = Blueprint("cos", __name__, url_prefix="/cos")

#process a single file
@cos_blueprint.route("/listCos/<prefix>", methods=["GET", "POST"])
@jwt_required()
def list_bucket_by_prefix(prefix):
    obj_cos= cos()
    bucket_list = obj_cos.list_bucket_documents(prefix)
    return bucket_list


