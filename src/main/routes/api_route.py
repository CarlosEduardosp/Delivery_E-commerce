from .imports_api_route import *  # noqa

api_routes_bp = Blueprint("api_routes", __name__)


@api_routes_bp.route(
    "/",
    defaults={"apelido": "Efetue_o_Login!", "quantidade_carrinho": "Vazio"},
    methods=["GET", "POST"],
)
@api_routes_bp.route("/<apelido>", methods=["GET", "POST"])
@api_routes_bp.route("/<apelido>/<quantidade_carrinho>/", methods=["GET", "POST"])
def home(apelido: str, quantidade_carrinho: int = "vazio"):
    """rota teste"""

    # buscando cliente pelo apelido
    response_cliente = flask_adapter_cliente(
        api_route=register_cliente_composer(),
        data={"apelido": apelido},
        action="select",
    )

    for i in response_cliente:
        # caso tenha um apelido valido, consulta quantidade de carrinho pelo apelido.
        if apelido != "Efetue o Login!":
            quantidade_carrinho = flask_adapter_carrinho(
                api_route=register_carrinho_composer(),
                data={"id_cliente": i.id_cliente},
                action="select_len",
            )

    # selecionando todos os produtos cadastrados
    produtos = flask_adapter_produto(
        api_route=register_produto_composer(), data=None, action="select_all"
    )

    # selecionando todos os arquivos de imagens cadastrados na pasta static
    path = "C:/meus projetos/DeliverySystem/CleanArchitecture/src/main/configs/static/"
    img = os.listdir(path)

    return render_template(
        "home.html",
        img=img,
        apelido=apelido,
        quantidade_carrinho=quantidade_carrinho,
        produtos=produtos,
    )


@api_routes_bp.route(
    "/login", defaults={"apelido": "Efetue_o_Login!"}, methods=["GET", "POST"]
)
@api_routes_bp.route("/login/<apelido>/<quantidade_carrinho>", methods=["GET", "POST"])
def login(apelido: str, quantidade_carrinho: str = "vazio"):
    """Realiza o login comparando os dados inseridos, com os da tabela Cliente."""

    # instancia clientes, HttpRequest e selct de todos os clientes.
    clientes = flask_adapter_cliente(
        register_cliente_composer(), data={}, action="select_all"
    )

    # request do email e senhao do form
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")

        # comparando senha digitada com senha salva no banco
        for cliente in clientes.body:
            if cliente.email == email and senha == cliente.senha:
                apelido = cliente.apelido

                # coletando quantidade de produtos no carrinho de clientes
                quantidade_carrinho = flask_adapter_carrinho(
                    api_route=register_carrinho_composer(),
                    data={"id_cliente": cliente.id_cliente},
                    action="select_len",
                )

                return redirect(
                    url_for(
                        "api_routes.home",
                        quantidade_carrinho=quantidade_carrinho,
                        apelido=apelido,
                    )
                )
        # exibi mensagem de erro caso senha ou email sejam inválidos.
        mensagem = "Usuário não encontrado ou senha incorreta!!"
        flash(mensagem)

    return render_template(
        "login.html", apelido=apelido, quantidade_carrinho=quantidade_carrinho
    )


@api_routes_bp.route(
    "/cadastrar_cliente",
    defaults={"apelido": "Efetue_o_Login!"},
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
        complemento = request.form.get("complemento")

        # realizando a pesquisa do cep.
        if cep_cliente:
            endereco = flask_adapter_buscar_cep(
                api_route=buscar_cep_composer(),
                data={"cep_cliente": cep_cliente},
                action="cep_cliente",
            )  # se o usuario digitar algum complemento.
            if complemento:
                session["complemento"] = complemento
            else:
                session["complemento"] = endereco[5]

        # comparação das senhas e retorna um valor boolean
        if senha and confirmar_senha:
            response_senha = validador_senha(senha, confirmar_senha)

            if not response_senha:
                flash("erro -- senhas não conferem !!")

            else:
                # registrar codigo no banco
                faker = Faker()
                codigo = faker.random_number(digits=4)
                flask_adapter_codigo(
                    api_route=register_codigo_composer(),
                    data={"codigo": codigo, "id_cliente": 1},
                    action="insert",
                )

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
            # salvando dados do cliente no banco
            cliente = session.get("dados_cliente")
            cliente_insert = flask_adapter_cliente(
                api_route=register_cliente_composer(),
                data={
                    "apelido": cliente[1],
                    "email": cliente[2],
                    "senha": cliente[3],
                    "cep_cliente": cliente[4],
                },
                action="insert",
            )

            # salvando endereço no banco
            complemento = session.get("complemento")
            endereco = session.get("endereco_cliente")
            flask_adapter_endereco(
                api_route=register_endereco_composer(),
                data={
                    "id_cliente": cliente[0],
                    "cep_cliente": endereco[0],
                    "estado": endereco[1],
                    "cidade": endereco[2],
                    "bairro": endereco[3],
                    "logradouro": endereco[4],
                    "complemento": complemento,
                },
                action="insert",
            )

            # deletando do banco o codigo validado pelo cliente
            flask_adapter_codigo(
                api_route=register_codigo_composer(),
                data={"id_cliente": cliente_insert.body.id_cliente},
                action="delete",
            )

            return redirect(
                url_for("api_routes.home", apelido=cliente[1], quantidade_carrinho=0)
            )

    return render_template("validacao_codigo.html", email=email)


@api_routes_bp.route("/produto/<apelido>.", methods=["GET", "POST"])
def produto(apelido: str):
    """endpoint para exibir produtos cadastrados"""

    return render_template("produtos.html", apelido=apelido)


@api_routes_bp.route("/sair/<apelido>", methods=["GET", "POST"])
def sair(apelido: str):
    """Função para encerrar o login. e o apelido passa a ser 'Efetue o login!'."""

    return redirect(url_for("api_routes.login", apelido="Efetue_o_Login!"))


@api_routes_bp.route("/testando/teste/denovo", methods=["GET", "POST"])
def teste():
    """teste"""

    data = {"id_cliente": 2}

    response_adapter = flask_adapter_cliente(api_route=register_cliente_composer())
    print(response_adapter)

    url = "http://127.0.0.1:5000/buscando/api/post"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(data), headers=headers)

    response_adapter = flask_adapter_cliente(api_route=register_cliente_composer())
    print(response_adapter)

    print("sucesso no envio", response)

    return render_template("teste.html")


@api_routes_bp.route("/buscando/api/post", methods=["GET", "POST"])
def buscar_api():
    response = flask_adapter_buscar_cep(
        api_route=buscar_cep_composer(),
        data={"cep_cliente": "26515570"},
        action="cep_cliente",
    )

    return response.cep_cliente
