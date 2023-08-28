# importing the sys module
import sys 
sys.path.append('')
from dotenv import dotenv_values,load_dotenv
from app.db.mongodb import MongoDB as mongo
from app.db.object_storage import ObjecStorage as cos
from app.services.auth_token.auth_token import Auth_login
import pytest
import os


ENV = dotenv_values(".env")
load_dotenv(override=False)
print("Env: ",ENV)


class TestUtilsPytest():
    
    def test_db_mongo(self):
        obj = mongo()
        assert str(obj.connection_database()) != "[ERROR] connection error"
        #self.assertNotEqual(str(self.create_switch_data_collection()),"[ERROR] connection error")
        #self.assertNotEqual(str(self.insert_one_value()),"[ERROR] connection error")
        #self.assertNotEqual(str(self.insert_one_value_users()),"[ERROR] connection error")

    