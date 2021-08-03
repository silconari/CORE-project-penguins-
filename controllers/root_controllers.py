from utils.handle_error import handle_error
from utils.json_response import json_response
from app import app
from flask import request


@app.route("/")
@handle_error
def example():
    penguin = {
        "id": 1
    }
    return json_response(penguin)


@app.route("/animal_info")
@handle_error
def animal_info_fn():
    print(request.args)
    species = request.args.get("species")
    island = request.args.get("island")
    raise ValueError("error")
    return {
        "species": species,
        "island": island,
    }
