import os
from dotenv import load_dotenv
from pymongo import MongoClient
import polars as pl
import pandas as pd
import pymongo

# if os.path.exists(".env"):
#     load_dotenv(".env")
# username = os.getenv("MONGODB_USER")
# password = os.getenv("MONGODB_PASSWORD")
# if not username:
#     raise ValueError("MONGODB_USER not set")
# if not password:
#     raise ValueError("MONGODB_PASSWORD not set")


# MongoDB connection parameters
mongo_host = 'tutorial-mongodb-1'
mongo_port = os.getenv("MONGODB_PORT")
mongo_user = os.getenv("MONGODB_USER")
mongo_pass = os.getenv("MONGODB_PASSWORD")
mongo_auth_source = 'admin' 

if not mongo_port:
    raise ValueError("MONGODB_PORT not set")
if not mongo_user:
    raise ValueError("MONGODB_USER not set")
if not mongo_pass:
    raise ValueError("MONGODB_PASSWORD not set")


client = pymongo.MongoClient(host=mongo_host,
                             port=mongo_port,
                             username=mongo_user,
                             password=mongo_pass,
                             authSource=mongo_auth_source)

# Check if MongoDB is reachable and authenticate
try:
    # List all databases in MongoDB
    databases = client.list_database_names()
    print("MongoDB connection successful. Databases available:", databases)
except pymongo.errors.ConnectionFailure:
    print("Failed to connect to MongoDB.")


def get_collection(layer: str, database: str) -> MongoClient:
    client = pymongo.MongoClient(host=mongo_host,
                             port=mongo_port,
                             username=mongo_user,
                             password=mongo_pass,
                             authSource=mongo_auth_source)
    db = client[layer]
    collection = db[database]
    return collection

def insert_document(collection: MongoClient, document: list[dict]) -> None:
    for doc in document:
        if '_id' in doc:
            # Update the existing document or insert a new document if no matching document is found
            collection.update_one({'_id': doc['_id']}, {'$set': doc}, upsert=True)
        else:
            # Insert a new document
            collection.insert_one(doc)

def store_data(layer: str, database: str, document: list[dict]) -> None:
    collection = get_collection(layer, database)
    insert_document(collection, document)

def get_all_data(layer: str, database: str) -> list[dict]:
    collection = get_collection(layer, database)
    return collection.find()

def get_dataframe_from_mongoDB(layer: str, database: str) -> pd.DataFrame:
    data = get_all_data(layer, database)
    return pd.DataFrame(data)
