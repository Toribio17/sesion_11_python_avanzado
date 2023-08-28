from pymongo import MongoClient
import os

class MongoDB():
    def __init__(self):
        print("Mongo constructor")

    def connection_database(self):
        
        try:
            client = MongoClient(os.environ["MONGO_CONNECTION"])
            #client = MongoClient(host='test_mongodb',ort=27017,username='root', password='rootpassword',authSource="admin")
            
            server_info = client.server_info()
        except:
            server_info = "[ERROR] connection error"
            client = server_info
        else:
            print("[Succesfully] connection ok")
        finally:
            return client
            


    def create_switch_data_collection(self):
        try:
            client = self.connection_database()
            #Creating a collection
            db = client['authorize']
            mongo_collection = db['user_access']  
            
        except:
            return "[ERROR] connection error"
        else:
            print("[Succesfully] connection ok")
            return mongo_collection,client
    
    def insert_one_value(self,name,age):
        try:
            mongo_collection,client = self.create_switch_data_collection()
            doc1 = {"name": name, "age": age}
            #Inserting document into a collection
            response_mongo = mongo_collection.insert_one(doc1)
            print("root:", response_mongo)
            self.close_database(client)
            
        except:
            return "[ERROR] connection error"
        else:
            return response_mongo
            
    
    def insert_one_value_users(self,user_doc):
        try:
            mongo_collection,client = self.create_switch_data_collection()
            doc1 = user_doc
            #Inserting document into a collection
            mongo_collection.insert_one(doc1)
            self.close_database(client)
        except:
            return "[ERROR] connection error"
        else:
            return "[Succesfully] INSERT connection ok"
    
    def find_one_data_value(self,column,value):
        mongo_collection,client = self.create_switch_data_collection()
        one_value = mongo_collection.find_one({column:value})
        self.close_database(client)
        
        return one_value

        
    def find_all_values(self):
        list_values = []
        mongo_collection,client = self.create_switch_data_collection()
        values =  mongo_collection.find()
        for value in values:
            list_values.append(value)
        
        self.close_database(client)
        
        return list_values
    
    def delete_one_value(self):
        mongo_collection,client = self.create_switch_data_collection()
        result_delete = mongo_collection.delete_one({"name":"Mr.Coder"})
        print(result_delete)
        self.close_database(client)
        
        return result_delete
        
    
    def close_database(self, mongo_client):
        mongo_client.close()

if __name__ == "__main__":
    obj_mongo = MongoDB()
    
    #create a collection 
    #obj_mongo.create_switch_data_collection()
    #obj_mongo.find_one_data_value("name","Mariana L")
    #obj_mongo.insert_one_value("Elizabeth Garcia",25)
    obj_mongo.find_all_values()