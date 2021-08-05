import os
from flask import Flask
from flask_pymongo import PyMongo
import streamlit as st
import requests
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

app = Flask("my_first_API")

username = os.getenv("ATLAS_USER")
password = os.getenv("ATLAS_PASSWORD")

app.config["MONGO_URI"] = f"mongodb+srv://{username}:{password}@cluster0.enltd.mongodb.net/test?authSource=admin&replicaSet=atlas-mrg0dm-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true"
mongo = PyMongo(app)

response = requests.get("http://127.0.01:3000/")
print(response.json())
data_table1 = pd.DataFrame(response.json())
st.write(data_table1)
