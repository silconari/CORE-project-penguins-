from flask import Response
import json


def json_response(data, status=500):
    return Response(
        json.dumps(data),
        mimetype="application/json",
        status=status

    )
