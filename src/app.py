import os
from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv
load_dotenv()

app = Flask("my_first_API")

username = os.getenv("ATLAS_USER")
password = os.getenv("ATLAS_PASSWORD")

app.config["MONGO_URI"] = url = f"mongodb+srv://{username}:{password}@cluster0.enltd.mongodb.net/test?authSource=admin&replicaSet=atlas-mrg0dm-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true"
mongo = PyMongo(app)
