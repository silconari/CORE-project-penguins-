from requests.api import get
import os
from werkzeug.wrappers import response
from utils.handle_error import handle_error
import json
from utils.json_response import json_response
from app import app
from flask import request
from utils.mongo_connect import get_mongo_db
from bson import json_util
import requests
import streamlit as st
from dotenv import load_dotenv
load_dotenv()


@app.route("/")
# @handle_error
def get_coll():
    penguins_coll = get_mongo_db().get_collection("penguins")
    return json_util.dumps(list(penguins_coll.find({})))


@app.route("/location")
# @handle_error
def get_geoquery():
    API_key = os.getenv("API_key")
    name = request.args["name"]
    geoquery = requests.get(
        f"http://api.positionstack.com/v1/forward?access_key={API_key}&query={name}")
    return json_util.dumps({"latitude": geoquery.json()["data"][0]["latitude"], "longitude": geoquery.json()["data"][0]["longitude"]})
