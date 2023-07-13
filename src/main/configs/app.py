from flask import Flask
from flask_cors import CORS
from src.main.routes.rotas.rotas_menu.route_home import api_routes_bp_home
from src.main.routes.rotas.rotas_menu.route_login import api_routes_bp_login
from src.main.routes.rotas.rotas_cliente.route_cadastrar_cliente import (
    api_routes_bp_cad_cliente,
)
from src.main.routes.rotas.rotas_cliente.route_validar_email import (
    api_routes_bp_validar,
)
from src.main.routes.rotas.rotas_produto.route_produto import api_routes_bp_produto
from src.main.routes.rotas.rotas_produto.route_cadastrar_produto import (
    api_routes_bp_cad_produto,
)
from src.main.routes.rotas.rotas_carrinho.route_carrinho import api_routes_bp_carrinho
from src.main.routes.rotas.rotas_carrinho.route_adicionar_carrinho import (
    api_routes_bp_adicionar_carrinho,
)
from src.main.routes.rotas.rotas_cliente.route_clientes import api_routes_bp_clientes
from src.main.routes.rotas.rotas_pedido.route_pedidos_cliente import (
    api_routes_bp_pedidos_cliente,
)
from src.main.routes.rotas.rotas_cliente.route_deletar_cliente import (
    api_routes_bp_del_cliente,
)
from src.main.routes.rotas.rotas_produto.route_deletar_produto import (
    api_routes_bp_del_produto,
)
from src.main.routes.rotas.rotas_carrinho.route_deletar_carrinho import (
    api_routes_bp_del_carrinho,
)
from src.main.routes.rotas.rotas_produto.route_editar_produto import (
    api_routes_bp_editar_produto,
)
from src.main.routes.rotas.rotas_cliente.route_perfil import api_routes_bp_perfil
from src.main.routes.rotas.rotas_pedido.route_pedido import api_routes_bp_pedido
from src.main.routes.rotas.rotas_pedido.route_confirmar_pedido import (
    api_routes_bp_confirmar_pedido,
)
from src.main.routes.rotas.rotas_menu.route_sair import api_routes_bp_sair
from src.main.routes.rotas.rotas_pedido.route_controle_pedido import (
    api_routes_bp_controle_pedido,
)

app = Flask(__name__)

CORS(app)

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
app.register_blueprint(api_routes_bp_del_cliente)
app.register_blueprint(api_routes_bp_del_produto)
app.register_blueprint(api_routes_bp_del_carrinho)
app.register_blueprint(api_routes_bp_editar_produto)
app.register_blueprint(api_routes_bp_perfil)
app.register_blueprint(api_routes_bp_pedido)
app.register_blueprint(api_routes_bp_confirmar_pedido)
app.register_blueprint(api_routes_bp_sair)
app.register_blueprint(api_routes_bp_controle_pedido)

app.secret_key = "b'\x92O7\x1a\x0e\x94\xb2\xff\x04\xdaD\x98)\xc79-'"
