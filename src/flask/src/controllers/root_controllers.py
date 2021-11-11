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
@handle_error
def get_coll_penguins():
    penguins_coll = get_mongo_db().get_collection("penguins")
    return json_util.dumps(list(penguins_coll.find({})))


@app.route("/penguins")
# @handle_error
def info_sex_penguins():

    penguin_sex = request.args.getlist("sex")
    penguin_species = request.args.getlist("species")
    penguins_coll = get_mongo_db().get_collection("penguins")
    penguins_info = {}

    if penguin_sex:
        penguins_info["Sex"] = {"$in": penguin_sex}
    if penguin_species:
        penguins_info["Species"] = {"$in": penguin_species}
    return json_util.dumps(list(penguins_coll.find(penguins_info)))


@ app.route("/islands")
@ handle_error
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


@ app.route("/location")
@ handle_error
def get_geoquery():
    API_key = os.getenv("API_key")
    name = request.args["name"]
    geoquery = requests.get(
        f"http://api.positionstack.com/v1/forward?access_key={API_key}&query={name}")
    return json_util.dumps({"latitude": geoquery.json()["data"][0]["latitude"], "longitude": geoquery.json()["data"][0]["longitude"]})
