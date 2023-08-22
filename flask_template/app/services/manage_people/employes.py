from app.db.cloudantdb import CloudantDB as cloudant

class Employes(cloudant):
    
    def __ini__(self):
        print("My conts")
        
    def get_all_employes(self):
        result_dict = self.get_all_documents()
        
        return result_dict