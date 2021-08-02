from flask import Response
import json


def json_response(data):
    return Response(
        json.dumps(data),
        mimetype="application/json"
    )
