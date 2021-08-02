from utils.json_response import json_response
from app import app


@app.route("/")
def example():
    penguin = {
        "id": 1
    }
    return json_response(penguin)
