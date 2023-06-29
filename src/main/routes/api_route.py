from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session,
)
from src.main.composer.register_produto_composer import register_produto_composer
from src.main.composer.buscar_cep_composer import buscar_cep_composer
from src.presenters.helpers.http_models import HttpRequest
from .functions import validador_senha, comparar_codigo
from src.data.enviar_codigo_email.enviar_codigo import EnviarCodigoEmail
from src.main.composer.register_codigo_composer import register_codigo_composer
from src.main.composer.register_cliente_composite import register_cliente_composer
from src.main.composer.register_carrinho_composer import register_carrinho_composer
from src.main.composer.register_endereco_composer import register_endereco_composer
from src.doman.models.cliente import Cliente
from src.main.adapter.flask_adapter_cliente import flask_adapter_cliente
from faker import Faker
import os

# import json


api_routes_bp = Blueprint("api_routes", __name__)


@api_routes_bp.route(
    "/",
    defaults={"apelido": "Efetue o Login!", "quantidade_carrinho": 0},
    methods=["GET", "POST"],
)
@api_routes_bp.route("/<apelido>/<quantidade_carrinho>/", methods=["GET", "POST"])
def home(apelido: str, quantidade_carrinho: int = 0):
    """rota teste"""

    # selecionando todos os produtos cadastrados
    http_request = HttpRequest()
    response = register_produto_composer()
    response = response.route_select_all(http_request)
    produtos = response.body

    # selecionando todos os arquivos de imagens cadastrados na pasta static
    path = "C:/meus projetos/DeliverySystem/CleanArchitecture/src/main/configs/static/"
    img = os.listdir(path)

    # recupera a quantidade de imagens na pasta
    # carrinho = len(img)
    return render_template(
        "home.html",
        img=img,
        apelido=apelido,
        quantidade_carrinho=quantidade_carrinho,
        produtos=produtos,
    )


@api_routes_bp.route(
    "/login", defaults={"apelido": "Efetue o Login!"}, methods=["GET", "POST"]
)
@api_routes_bp.route("/login/<apelido>/<quantidade_carrinho>", methods=["GET", "POST"])
def login(apelido: str, quantidade_carrinho: int = 0):
    """Realiza o login comparando os dados inseridos, com os da tabela Cliente."""

    # instancia clientes, HttpRequest e selct de todos os clientes.
    http_request = HttpRequest()
    clientes = register_cliente_composer()
    clientes = clientes.route_select_all(http_request)

    # request do email e senhao do form
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")

        # comparando senha digitada com senha salva no banco
        for cliente in clientes.body:
            if cliente.email == email and senha == cliente.senha:
                apelido = cliente.apelido

                # coletando quantidade de produtos no carrinho de clientes
                http_request_carrinho = HttpRequest(
                    query={"id_cliente": cliente.id_cliente}
                )
                quantidade_carrinho = register_carrinho_composer()
                response = quantidade_carrinho.route_select(http_request_carrinho)
                carrinho = []
                for i in response.body:
                    carrinho.append(i)
                carrinho = len(carrinho)

                return redirect(
                    url_for(
                        "api_routes.home", quantidade_carrinho=carrinho, apelido=apelido
                    )
                )
            else:
                mensagem = "Usuário não encontrado ou senha incorreta!!"
                flash(mensagem)

    return render_template(
        "login.html", apelido=apelido, quantidade_carrinho=quantidade_carrinho
    )


@api_routes_bp.route(
    "/cadastrar_cliente",
    defaults={"apelido": "Efetue o Login!"},
    methods=["GET", "POST"],
)
@api_routes_bp.route("/cadastrar_cliente/<apelido>", methods=["GET", "POST"])
def cadastrar_cliente(apelido: str):
    """tela de cadastro de cliente"""

    endereco = ["---", "---", "---", "---", "---"]

    email = ""

    # request dos dados do usuario via formulario.
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")
        confirmar_senha = request.form.get("confirmar_senha")
        apelido = request.form.get("apelido")
        cep_cliente = request.form.get("end")
        # complemento_form = request.form.get("complemento")

        # realizando a pesquisa do cep.
        if cep_cliente:
            response = buscar_cep_composer()
            http_request = HttpRequest(query={"cep_cliente": cep_cliente})
            endereco = response.route_buscar_cep(http_request)
            endereco = endereco.body

        # comparação das senhas e retorna um valor boolean
        if senha and confirmar_senha:
            response_senha = validador_senha(senha, confirmar_senha)

            if not response_senha:
                flash("erro -- senhas não conferem !!")

            else:
                # enviando codigo para o email cadastrado
                faker = Faker()
                codigo = faker.random_number(digits=4)
                http_request = HttpRequest(query={"codigo": codigo, "id_cliente": 1})
                registrar_codigo = register_codigo_composer()
                registrar_codigo.route_insert(http_request)
                enviar_codigo = EnviarCodigoEmail()
                enviar_codigo.enviar_email_codigo(
                    codigo=codigo, email_destinatario=email
                )

                dados_cliente = Cliente(
                    id_cliente=0,
                    apelido=apelido,
                    email=email,
                    senha=senha,
                    cep_cliente=cep_cliente,
                )

                # guardando os dados do cliente
                session["dados_cliente"] = dados_cliente
                session["endereco_cliente"] = endereco
                return render_template("validacao_codigo.html", email=email)

    return render_template(
        "cadastrar_cliente.html", email=email, apelido=apelido, endereco=endereco
    )


@api_routes_bp.route("/validar/<email>", methods=["GET", "POST"])
def validar_email(email: str):
    """validar o codigo enviado para o email"""

    # request do valor do codigo via form
    if request.method == "POST":
        codigo = request.form.get("codigo")

        # validação do codigo, com o codigo cadastrado
        response = comparar_codigo(codigo)
        if response:
            http_request = HttpRequest(query={"id_cliente": 1, "codigo": codigo})
            response_codigo = register_codigo_composer()
            response_codigo.route_delete(http_request)

            # dados salvos do cliente
            dados_cliente = session.get("dados_cliente")
            http_request_cliente = HttpRequest(
                query={
                    "apelido": dados_cliente[1],
                    "email": dados_cliente[2],
                    "senha": dados_cliente[3],
                    "cep_cliente": dados_cliente[4],
                }
            )

            # salvando od dados no banco de dados.
            response_inserir_cliente_bd = register_cliente_composer()
            response_cliente_bd = response_inserir_cliente_bd.route_insert(
                http_request_cliente
            )
            cliente = []
            for i in response_cliente_bd.body:
                cliente.append(i)

            endereco = session.get("endereco_cliente")

            http_endereco = HttpRequest(
                query={
                    "id_cliente": cliente[0],
                    "cep_cliente": endereco[0],
                    "estado": endereco[1],
                    "cidade": endereco[2],
                    "bairro": endereco[3],
                    "logradouro": endereco[4],
                    "complemento": endereco[5],
                }
            )
            registrar_endereco = register_endereco_composer()
            registrar_endereco.route_insert(http_endereco)
            return redirect(
                url_for(
                    "api_routes.home", apelido=dados_cliente[1], quantidade_carrinho=0
                )
            )

    return render_template("validacao_codigo.html", email=email)


@api_routes_bp.route("/sair/<apelido>", methods=["GET", "POST"])
def sair(apelido: str):
    """Função para encerrar o login. e o apelido passa a ser 'Efetue o login!'."""

    return redirect(url_for("api_routes.login", apelido="Efetue o Login!"))


@api_routes_bp.route("/testando/teste/denovo", methods=["GET", "POST"])
def teste():
    """teste"""

    dados = {
        "id_cliente": 1,
        "apelido": "Carlos Eduardo",
        "email": "carlos.spadilha@yahoo.com.br",
        "senha": "01254",
        "cep_cliente": "26515570",
    }
    response = flask_adapter_cliente(
        api_route=register_cliente_composer(), data=dados, action="select"
    )

    print(response)
    if response.body:
        for i in response.body:
            print(i)

    return render_template("teste.html")
