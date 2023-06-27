from flask import Flask
from flask_cors import CORS
from src.main.routes.api_route import api_routes_bp

app = Flask(__name__)

CORS(app)

app.register_blueprint(api_routes_bp)

app.secret_key = "b'\x92O7\x1a\x0e\x94\xb2\xff\x04\xdaD\x98)\xc79-'"
