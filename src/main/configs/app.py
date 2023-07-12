from flask import Flask
from flask_cors import CORS
from src.main.routes.api_route import api_routes_bp
from src.main.routes.rotas.route_home import api_routes_bp_home
from src.main.routes.rotas.route_login import api_routes_bp_login
from src.main.routes.rotas.route_cadastrar_cliente import api_routes_bp_cad_cliente
from src.main.routes.rotas.route_validar_email import api_routes_bp_validar
from src.main.routes.rotas.route_produto import api_routes_bp_produto
from src.main.routes.rotas.route_cadastrar_produto import api_routes_bp_cad_produto
from src.main.routes.rotas.route_carrinho import api_routes_bp_carrinho
from src.main.routes.rotas.route_adicionar_carrinho import (
    api_routes_bp_adicionar_carrinho,
)
from src.main.routes.rotas.route_clientes import api_routes_bp_clientes
from src.main.routes.rotas.route_pedidos_cliente import api_routes_bp_pedidos_cliente


app = Flask(__name__)

CORS(app)

app.register_blueprint(api_routes_bp)
app.register_blueprint(api_routes_bp_home)
app.register_blueprint(api_routes_bp_login)
app.register_blueprint(api_routes_bp_cad_cliente)
app.register_blueprint(api_routes_bp_validar)
app.register_blueprint(api_routes_bp_produto)
app.register_blueprint(api_routes_bp_cad_produto)
app.register_blueprint(api_routes_bp_carrinho)
app.register_blueprint(api_routes_bp_adicionar_carrinho)
app.register_blueprint(api_routes_bp_clientes)
app.register_blueprint(api_routes_bp_pedidos_cliente)

app.secret_key = "b'\x92O7\x1a\x0e\x94\xb2\xff\x04\xdaD\x98)\xc79-'"
