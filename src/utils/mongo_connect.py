import os
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()


def get_mongo_db():
    username = os.getenv("ATLAS_USER")
    password = os.getenv("ATLAS_PASSWORD")

    url = f'mongodb+srv://{username}:{password}@cluster0.enltd.mongodb.net/test?authSource=admin&replicaSet=atlas-mrg0dm-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true'
    client = MongoClient(url)

    return client.get_database("penguins-data")
