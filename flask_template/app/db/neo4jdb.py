from dotenv import dotenv_values,load_dotenv
from neo4j import GraphDatabase
import os

class Neo4J():
    
    def __init__(self):
        print("Neo4J class")
        
    def neo4js_connection(self):
        URI = os.environ['NEO4J_HOST']
        
        driver = GraphDatabase.driver(URI, auth=(os.environ['NEO4J_USER_NAME'], os.environ['NEO4J_PASSWORD']))
        driver.verify_connectivity() 
        db = driver.session(database=os.environ['NEO4J_DATABASE'])
        
        return db,driver
    
    def insert_node_query(self):
        list_neo4j = self.neo4js_connection()
        db = list_neo4j[0]
        driver = list_neo4j[1]
        
        properties = "{name: 'Jeniffer', yearsExperience: 5}"
        query = "CREATE (Jeniffer:People {properties})"
        query = query.format(Jeniffer="People", properties=properties)
        
        db.run(query)
        
        self.close_db(driver)
        
    def insert_relationship_query(self):
        list_neo4j = self.neo4js_connection()
        db = list_neo4j[0]
        driver = list_neo4j[1]
        
        query ="MATCH (j:People {name: 'Jeniffer'})" + "MATCH (m:People {name: 'Sally'})" + "MERGE (j)-[r:IS_FRIENDS_WITH]->(m)"
        db.run(query)
        
        self.close_db(driver)
        
    def list_node(self):
        list_neo4j = self.neo4js_connection()
        db = list_neo4j[0]
        driver = list_neo4j[1]
        
        query = "MATCH (x:People) RETURN x"
        nodes = db.run(query)
        
        for node in nodes:
            print("node: ",node)
        
        self.close_db(driver)
        
    def close_db(self,driver):
        driver.close()

        
if __name__ == '__main__':
    #declarar variable de entorno
    ENV = dotenv_values("/Users/luistoribio/Documents/curso_python_avanzado/sesion_11_python_avanzado/flask_template/.env")
    load_dotenv(override=False)
    print("Env: ",ENV)
    
    obj = Neo4J()
    #obj.neo4js_connection()
    #obj.insert_node_query()
    #obj.insert_relationship_query()
    obj.list_node()