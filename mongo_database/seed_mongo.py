from pymongo import MongoClient
import json
import os

def seed_database(mongo_url, db_name, collection_name):
    client = MongoClient(mongo_url)
    database = client[db_name]
    collection = database[collection_name]
    f = open(os.getenv('BOOKS_50_PATH'))
    collection.insert_many(json.load(f))
    f.close()
    return collection