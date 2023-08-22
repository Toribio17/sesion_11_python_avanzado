from app.db.object_storage import ObjecStorage as cos

class ObjectStorageServices(cos):
    
    def __init__(self):
        print("My COS services")
        
    def list_bucket_documents(self,prefix):
        bucket_prefix_list = self.read_object_storage_list(prefix)
        
        return bucket_prefix_list
            
    def read_object_storage_list(self,prefix):
        document_list = []
        list_of_file = self.list_documents_by_prefix(prefix)
        for file in list_of_file:
            document_list.append(file.key)
        return document_list
            
            


if __name__ == '__main__':
    obj = ObjectStorageServices()
    obj.list_documents()