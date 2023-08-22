from app.db.mongodb import MongoDB as mongo
import json
from bson import json_util

class Students(mongo):
    
    def __init__(self):
        print("Hi")
        
        
    def get_all_student(self):
        student_dict = self.find_all_values()
        student_dict = self.convert_to_json(student_dict)
        
        return student_dict
    
    def get_one_student(self,field,value):
        student_dict = self.find_one_data_value(field,value)
        student_dict = self.convert_to_json(student_dict)
        print("services",student_dict)
        
        return student_dict
        
    
    def convert_to_json(self,mongo_reponse):
        ##Dump loaded Binary to valid JSON string and reload it as dict
        mongo_dict = json.loads(json_util.dumps(mongo_reponse))
        
        return mongo_dict
        