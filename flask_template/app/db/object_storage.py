import boto3, botocore
from boto3.exceptions import S3UploadFailedError
from botocore.exceptions import ClientError
import os
from dotenv import dotenv_values,load_dotenv

class ObjecStorage():
    
    def __init__(self):
        print("constructor")
        
    
    def object_storage_connection(self):
        try:
            endpoint = os.environ["COS_ENDPOINT"]
            s3 = boto3.resource('s3', endpoint_url=endpoint)
            client = boto3.client('s3', region_name=os.environ['REGION_OBJECT'], endpoint_url=endpoint)
            
        except ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object does not exist.")
                print(e)
            
            return "[ERROR] COS connection error"
        else:
            return s3,client
            
                
                
    def list_documents_by_prefix(self,prefix):
        connection = self.object_storage_connection()
        s3 = connection[0]
        try:
            current_bucket = s3.Bucket(os.environ['BUCKET_NAME'])
            bucket_list = current_bucket.objects.filter(Prefix=prefix).all()
            
        except ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object does not exist.")
        else:
            print("[SUCCESSFULLY] completed the process")
            return bucket_list

                
    def download_document(self,file_name,folder_output,prefix):
        try:
            str_size = len(prefix)   
            connection = self.object_storage_connection()
            client = connection[1]
            path_folder = self.join_paths(os.environ["GENERAL_PATH"],os.environ['PATH_OBJECT_STORAGE'] + "/" + folder_output)
            path_file = self.join_paths(path_folder,file_name)
            if str_size > 0:
                file_name = prefix + "/" + file_name
            client.download_file(Bucket=os.environ['BUCKET_NAME'], 
                                 Key=file_name,
                                 Filename=path_file)

        except ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object does not exist.")
            return "[ERROR] COS connection error"
        else:
            print("[SUCCESSFULLY] DOWNLOAD completed the process",file_name)
            return "[SUCCESSFULLY] COS connection download"

            
    def upload_document(self,file_name,folder_source,prefix):
        try:
            str_size = len(prefix)
            connection = self.object_storage_connection()
            client = connection[1]
            path_folder = self.join_paths(os.environ["GENERAL_PATH"],os.environ['PATH_OBJECT_STORAGE'] + "/" + folder_source)
            path_file = self.join_paths(path_folder,file_name)
            if str_size > 0:
                file_name = prefix + "/" + file_name
            client.upload_file(Filename=path_file,
                               Bucket=os.environ['BUCKET_NAME'], 
                               Key=file_name)
            
        except ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object does not exist.")
                
            return "[ERROR] COS connection error"
        else:
            print("[SUCCESSFULLY] UPLOAD completed the process",file_name)
            return "[SUCCESSFULLY] COS connection Upload"
          
            
    def delete_document(self,file_name,prefix):
        try:
            str_size = len(prefix)
            connection = self.object_storage_connection()
            client = connection[1]
            if str_size > 0:
                file_name = prefix + "/" + file_name
            client.delete_object(Bucket=os.environ['BUCKET_NAME'], Key=file_name)
            
        except ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object does not exist.")
        else:
            print("[SUCCESFULL] DELETE completed the process",file_name)
            
    def join_paths(self,string_1,string_2):
        path_folder = os.path.join(string_1,string_2)
        
        return path_folder
            
if __name__ == '__main__':
    #declarar variable de entorno
    ENV = dotenv_values("/Users/luistoribio/Documents/curso_python_avanzado/sesion_11_python_avanzado/flask_template/.env")
    load_dotenv(override=False)
    print("Env: ",ENV)
    
    obj = ObjecStorage()
    #obj.upload_document("example_2.pdf","input_files","input_files_2")
    #obj.download_document("example_2.pdf","output_files","input_files_2")
    obj.delete_document("example-1.pdf")