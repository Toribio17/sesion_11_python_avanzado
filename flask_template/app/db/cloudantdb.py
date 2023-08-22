from ibmcloudant.cloudant_v1 import CloudantV1,Document
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os

class CloudantDB():
    
    def __init__(self):
        print("Cloudant constructor")
    
    def generate_connection(self):
        authenticator = IAMAuthenticator(os.environ['CLOUDANT_APIKEY'])
        service = CloudantV1(authenticator = authenticator)
        service.set_service_url(os.environ['CLOUDANT_URL'])

        return service
    
    
    def insert_document(self,name,last_name,age,job_role):
        service = self.generate_connection()
        document = Document(
            name=name,
            last_name=last_name,
            age=age,
            job_role=job_role
        )
        
        response = service.post_document(db='employe', document=document).get_result()
        
        return response
    
    def get_all_documents(self):
        service = self.generate_connection()
        
        response = service.post_all_docs(
            db='employe',
            include_docs=True,
            limit=10).get_result()
        
        print(response)
        
        return response
    
    
if __name__ == "__main__":
    obj_cloudant = CloudantDB()
    #obj_cloudant.insert_document("Belen","Cravioto",31,"CEO")
    obj_cloudant.get_all_documents()
        
    