from flask import Blueprint, render_template
from src.main.composer.register_produto_composer import register_produto_composer
from src.presenters.helpers.http_models import HttpRequest
import os

api_routes_bp = Blueprint("api_routes", __name__)


@api_routes_bp.route("/", methods=["GET"])
def home():
    """rota teste"""

    http_request = HttpRequest()
    response = register_produto_composer()
    response = response.route_select_all(http_request)
    produtos = response.body

    path = "C:/meus projetos/DeliverySystem/CleanArchitecture/src/main/configs/static/"
    img = os.listdir(path)

    # recupera a quantidade de imagens na pasta
    carrinho = len(img)
    print(carrinho)
    return render_template(
        "home.html", img=img, apelido="kadu", quantidade_carrinho=2, produtos=produtos
    )


@api_routes_bp.route("/login", methods=["GET"])
def login():
    """tela login"""

    return render_template("login.html", quantidade_carrinho=3)


@api_routes_bp.route("/teste", methods=["GET"])
def teste():
    """tela teste"""

    return render_template("cadastrar_cliente.html")
