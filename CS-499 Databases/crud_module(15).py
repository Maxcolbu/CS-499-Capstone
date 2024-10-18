from pymongo import MongoClient

class AnimalShelter:
    """ CRUD operations for Animal collection in MongoDB """
   
    def __init__(self, user, password, host, port, db, collection):
        self.client = MongoClient(f'mongodb://{user}:{password}@{host}:{port}/?authSource=admin')
        self.database = self.client[db]
        self.collection = self.database[collection]
    
    def create(self, data):
        if data:
            result = self.collection.insert_one(data)
            return True if result.acknowledged else False
        else:
            raise ValueError("Data parameter is empty")
           
    def read(self, query=None):
        if query is None or not query:
            query = {}
        results = list(self.collection.find(query))
        return results
           
    def update(self, query, update_data):
        if query and update_data:
            result = self.collection.update_many(query, {'$set': update_data})
            return result.modified_count
        else:
            raise ValueError("Query or update_data parameter is empty")
            
    def delete(self, query):
        if query:
            result = self.collection.delete_many(query)
            return result.deleted_count
        else:
            raise ValueError("Query parameter is empty")