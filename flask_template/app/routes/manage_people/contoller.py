from flask import Blueprint
from app.services.manage_people.students import Students as student
from app.services.manage_people.employes import Employes as employe
from flask_jwt_extended import jwt_required

people_blueprint = Blueprint("people", __name__, url_prefix="/people")

#process a single file
@people_blueprint.route("/allStudents", methods=["GET", "POST"])
#@jwt_required()
def get_all_students():
    obj_student = student()
    student_response = obj_student.get_all_student()
    
    return student_response

#to send two variables use this format on browser /oneStudent/age&&31
@people_blueprint.route("/oneStudent/<field>&&<student_name>", methods=["GET", "POST"])
@jwt_required()
def get_one_student(field,student_name):
    obj_student = student()
    print(student_name)
    student_response = obj_student.get_one_student(field,student_name)
    
    return student_response

@people_blueprint.route("/allEmployes", methods=["GET", "POST"])
@jwt_required()
def get_all_employes():
    obj_employe = employe()
    employe_response = obj_employe.get_all_employes()
    print(employe_response)
    
    return employe_response

