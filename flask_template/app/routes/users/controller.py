from flask import Blueprint, jsonify
from app.services.users.users import Users

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/users', methods=['GET', 'POST'])
def list_users():
    users = Users()
    response = users.get_users()
    
    return jsonify(response)