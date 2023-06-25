from flask import Blueprint, render_template, request, redirect, url_for
from src.main.composer.register_produto_composer import register_produto_composer
from src.main.composer.buscar_cep_composer import buscar_cep_composer
from src.presenters.helpers.http_models import HttpRequest
import os
from .functions import validador_senha, criar_codigo_confirmacao, comparar_codigo


api_routes_bp = Blueprint("api_routes", __name__)


@api_routes_bp.route("/", methods=["GET", "POST"])
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


@api_routes_bp.route("/login", methods=["GET", "POST"])
def login():
    """tela login"""

    return render_template("login.html", quantidade_carrinho=3)


@api_routes_bp.route("/cadastrar_cliente", methods=["GET", "POST"])
def cadastrar_cliente():
    """tela de cadastro de cliente"""

    endereco = ["---", "---", "---", "---", "---"]
    email = ""
    apelido = ""

    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")
        confirmar_senha = request.form.get("confirmar_senha")
        apelido = request.form.get("apelido")
        cep_cliente = request.form.get("end")
        # complemento_form = request.form.get("complemento")

        # realizando a pesquisa do cep.
        response = buscar_cep_composer()
        http_request = HttpRequest(query={"cep_cliente": cep_cliente})
        endereco = response.route_buscar_cep(http_request)
        endereco = endereco.body

        # comparação das senhas e reto
        response = validador_senha(senha, confirmar_senha)

        if response:
            response = criar_codigo_confirmacao()

    return render_template(
        "cadastrar_cliente.html", email=email, apelido=apelido, endereco=endereco
    )


@api_routes_bp.route("/validar/<email>", methods=["GET", "POST"])
def validar_email(email: str):
    """validar o codigo enviado para o email"""

    if request.method == "POST":
        codigo = request.form.get("codigo")

        response = comparar_codigo(codigo)
        if response:
            return redirect(url_for("api_routes.home"))

    return render_template("validacao_codigo.html", email=email)


@api_routes_bp.route("/teste")
def teste():
    """teste"""

    return render_template("teste.html")
