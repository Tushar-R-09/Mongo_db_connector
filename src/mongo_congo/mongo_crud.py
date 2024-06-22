from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class mongo_connect:
    def __init__(self, url:str, database_name : str, collection_name : str):
        self.url = url
        self.database_name = database_name
        self.collection_name = collection_name
        self.client = MongoClient(self.url)
        self.database = self.client[self.database_name]
        self.collection = self.database[self.collection_name]

    def insert_record(self,record):
        if type(record) == list:
            for r in record:
                if type(r) != dict:
                    raise TypeError("Record must be a dictionary")
            self.collection.insert_many(record)

        else:
            if type(record) != dict:
                raise TypeError("Record must be a dictionary")
            self.collection.insert_one(record)
        return 
