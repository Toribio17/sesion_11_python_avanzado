from flask import Flask
from flask_cors import CORS
from app.routes.ocr.controller import ocr_blueprint as ocr_class
from app.routes.manage_people.contoller import people_blueprint
from app.routes.auth_token.controller import auth_blueprint
from app.routes.object_storage.controller import cos_blueprint
from dotenv import dotenv_values,load_dotenv
from flask_jwt_extended import JWTManager
import os

app = Flask(__name__)

#----------declarar variable de entorno----------
ENV = dotenv_values(".env")
load_dotenv(override=False)
print("Env: ",ENV)
#-------------------------------------------------

CORS(app,supports_credentials=True)
app.config["JWT_SECRET_KEY"] = os.environ['JWT_KEY']# Change this "super secret" with something else!
jwt = JWTManager(app)

app.register_blueprint(ocr_class)
app.register_blueprint(people_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(cos_blueprint)

@app.route('/', methods=['GET', 'POST'])
def hello():
    return "hello the services is working"