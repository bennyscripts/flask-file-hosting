import flask
import importlib
import os

from utils.config import Config

app = flask.Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = os.urandom(24)
Config.check()

for route_file in os.listdir("routes"):
    if route_file.endswith(".py"):
        lib = importlib.import_module(f"routes.{route_file[:-3]}")
        app.register_blueprint(lib.blueprint)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
