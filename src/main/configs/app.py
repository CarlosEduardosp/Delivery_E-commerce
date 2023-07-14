from flask import Flask
from flask_cors import CORS
from src.main.configs.register_blueprint.register_blueprint import RegisterBlueprint

app = Flask(__name__)

CORS(app)

RegisterBlueprint(app)

app.secret_key = "b'\x92O7\x1a\x0e\x94\xb2\xff\x04\xdaD\x98)\xc79-'"
