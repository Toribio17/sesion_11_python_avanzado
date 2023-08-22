import hashlib
from  app.db.mongodb import MongoDB as mongo
from flask_jwt_extended import create_access_token
import datetime

class Auth_login(mongo):
    
    def __init__(self):
        print("My tokens")
        
    def hash_encrypt(self,password):
        password=password.encode('utf-8')
        #Returns the encoded data in hexadecimal format
        haserh=hashlib.sha256(password).hexdigest()
        return haserh

    def confirm_login(self , password , password_encryted):
        loggin=False
        password_encryted_temp = self.hash_encrypt(password)
        if password_encryted == password_encryted_temp:
            loggin=True
        else :
            loggin == False

        return loggin
    
    def create_token(self,user_name,passsword,user_level_access,life_time_token):
        message_return = {}
        field = "user"
        try:
            register_value = self.find_one_data_value(field,user_name)
            login_state = self.confirm_login(passsword,register_value['password_encryted'])
            print(login_state)
            if login_state == True:
                additional_claims = {"user_level_access": user_level_access, "life_time_token": life_time_token}
                access_token = create_access_token(identity=user_name,additional_claims=additional_claims,fresh=datetime.timedelta(days=2),expires_delta=datetime.timedelta(days=2))
                message_return = {"token": access_token, "user_id": user_name }
            else:
                message_return = {"message":"user or login error","status":"520"}
            
            return message_return
                
        except Exception as e:
            print("[ERORR]: Token", e)
            message_return = {"error":"bad credentials","status":"207"}
        
        
    def create_user(self,user_name,password,level,mail):
        password = self.hash_encrypt(password)
        message_return = {}
        user_doc={
            "user": user_name,
            "password_encryted": password,
            "level": level,
            "mail":mail
            }
        field = "user"
        mongo_response = self.find_one_data_value(field,user_name)
        if mongo_response == None:
            self.insert_one_value_users(user_doc)
            message_return = {"user_created":True,"status":"200"}
        else:
            message_return = {"user_created":False,"status":"300"}
        
        return message_return
    
if __name__ == "__main__":
    obj = Auth_login()
    obj.create_user("Charmander","PythonAvanzado1","1","jose17tn@outlook.com")
    
        
    
        
        
        
        
        