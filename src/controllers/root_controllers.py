from requests.api import get
from utils.handle_error import handle_error
import json
from utils.json_response import json_response
from app import app
from flask import request
from utils.mongo_connect import get_mongo_db
from bson import json_util


@app.route("/")
@handle_error
def get_coll():
    penguins_coll = get_mongo_db().get_collection("penguins")
    return json_util.dumps(list(penguins_coll.find({})))
