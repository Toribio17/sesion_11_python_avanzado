# importing the sys module
import sys 
sys.path.append('/Users/luistoribio/Documents/curso_python_avanzado/sesion_11_python_avanzado/flask_template')
from dotenv import dotenv_values,load_dotenv
from app.db.mongodb import MongoDB as mongo
from app.db.object_storage import ObjecStorage as cos
from app.services.auth_token.auth_token import Auth_login
#import pytest
import unittest
import os


class TestUtils(unittest.TestCase,Auth_login,cos,mongo):
    
    def read_object_storage_list(self):
        file_value = ""
        list_of_file = self.list_documents_by_prefix("input_files")
        for file in list_of_file:
            if file.key == "input_files/example_2.pdf":
                file_value = file.key
        return file_value
                
    
    @unittest.skip("testing another one")
    def test_db_mongo(self):
        self.assertNotEqual(str(self.connection_database()),"[ERROR] connection error")
        self.assertNotEqual(str(self.create_switch_data_collection()),"[ERROR] connection error")
        self.assertNotEqual(str(self.insert_one_value("Jorge C","40")),"[ERROR] connection error")
        self.assertNotEqual(str(self.insert_one_value_users({"name": "name", "age": "age"})),"[ERROR] connection error")
        
    def test_db_object(self):
        self.assertNotEqual(self.object_storage_connection(),"[ERROR] COS connection error")
        self.assertEqual(self.read_object_storage_list(),"input_files/example_2.pdf")
        self.assertEqual(self.download_document("example_2.pdf","output_files","input_files"),"[SUCCESSFULLY] COS connection download")
        
    def test_services_auth(self):
        self.assertEqual(self.hash_encrypt(os.environ['JWT_TOKEN_PASSWORD']),os.environ['JWT_TOKEN_PASSWORD_ENCRYPTED'])
        self.assertTrue(self.confirm_login(os.environ['JWT_TOKEN_PASSWORD'],os.environ['JWT_TOKEN_PASSWORD_ENCRYPTED']))
        message_response = self.create_user("user_test","testing_value","1","testing@gmail.com")
        print(message_response['user_created'])
        self.assertTrue(message_response['user_created'])
        self.assertFalse(message_response['user_created'])
        
if __name__ == '__main__':
    
    ENV = dotenv_values(".env")
    load_dotenv(override=False)
    print("Env: ",ENV)
    
    unittest.main(failfast=False)
    #pytest.main()

