from config import PORT
import controllers.root_controllers
from json import load
from app import app


app.run("0.0.0.0", PORT, debug=True)
