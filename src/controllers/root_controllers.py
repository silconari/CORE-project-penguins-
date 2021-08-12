from requests.api import get
import os
from utils.handle_error import handle_error
from app import app
from flask import request
from utils.mongo_connect import get_mongo_db
from bson import json_util
import requests
from dotenv import load_dotenv
load_dotenv()


@app.route("/")
# @handle_error
def get_coll_penguins():
    penguins_coll = get_mongo_db().get_collection("penguins")
    return json_util.dumps(list(penguins_coll.find({})))


@app.route("/islands")
# @handle_error
def get_coll_islands():
    lat_lon = request.args["latlon"].split(",")
    lat_lon = [float(e) for e in lat_lon]
    islands_coll = get_mongo_db().get_collection("islands")
    return json_util.dumps(
        list(
            islands_coll.find(
                {
                    "location": {
                        "$near": {
                            "$geometry": {
                                "type": "Point",
                                "coordinates": lat_lon
                            },
                        }
                    }
                }
            )
        )[0]
    )


@app.route("/location")
# @handle_error
def get_geoquery():
    API_key = os.getenv("API_key")
    name = request.args["name"]
    geoquery = requests.get(
        f"http://api.positionstack.com/v1/forward?access_key={API_key}&query={name}")
    return json_util.dumps({"latitude": geoquery.json()["data"][0]["latitude"], "longitude": geoquery.json()["data"][0]["longitude"]})
