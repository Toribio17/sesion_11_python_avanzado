from flask import Blueprint
from app.services.auth_token.auth_token import Auth_login as auth
from  app.db.mongodb import MongoDB as mongo
from flask import request

auth_blueprint = Blueprint("authorize", __name__, url_prefix="/auth")

@auth_blueprint.route("/token", methods=["GET", "POST"])
def create_token():
    obj_auth = auth()
    username = str(request.json.get("username"))
    password = str(request.json.get("password"))
    user_level_access = str(request.json.get("user_access_level"))
    life_time_token = str(request.json.get("life_time_token"))
    message_return = {}
    try:
        if len(username) == 0:
            message_return = {"error":"bad credentials","satus":"407"}
        else:
            message_return = obj_auth.create_token(username,password,user_level_access,life_time_token)
            
        return message_return

    except Exception as e:
        print(e)
        return {"error":"bad credentials","status":"207"}

@auth_blueprint.route("/createUser", methods=["POST","GET"])
def create_user():
    user_name = str(request.json.get("username", None))
    password = str(request.json.get("password", None))
    level = str(request.json.get("level", None))
    mail= str(request.json.get("mail", None))
    
    obj_auth = auth()
    obj_auth.create_user(user_name,password,level,mail)
