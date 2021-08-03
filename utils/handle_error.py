from .json_response import json_response


def handle_error(fn):
    def wrapper():
        try:
            return fn()
        except Exception as e:
            print("An error has occurred")
            return json_response({"error": str(e)}, 500)
    wrapper.__name__ = fn.__name__
    return wrapper
