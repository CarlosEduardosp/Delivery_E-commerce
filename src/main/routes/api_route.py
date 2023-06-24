from flask import Blueprint, render_template

api_routes_bp = Blueprint("api_routes", __name__)


@api_routes_bp.route("/", methods=["GET"])
def home():
    """rota teste"""

    apelido = "Carol"
    quantidade_carrinho = 3
    return render_template(
        "base.html", apelido=apelido, quantidade_carrinho=quantidade_carrinho
    )


@api_routes_bp.route("/login", methods=["GET"])
def login():
    """tela login"""

    return render_template("login.html", quantidade_carrinho=3)


@api_routes_bp.route("/teste", methods=["GET"])
def teste():
    """tela teste"""

    return render_template("cadastrar_cliente.html")
