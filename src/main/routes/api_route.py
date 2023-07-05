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
    cliente = AdapterCliente(
        api_route=register_cliente_composer(), data={"apelido": apelido}
    )
    response_cliente = cliente.select()

    for i in response_cliente.body:
        # caso tenha um apelido valido, consulta quantidade de carrinho pelo apelido.
        if apelido != "Efetue o Login!":
            quantidade_carrinho = AdapterCarrinho(
                api_route=register_carrinho_composer(),
                data={"id_cliente": i.id_cliente},
            )
            quantidade_carrinho = quantidade_carrinho.select()
            quantidade_carrinho = quantidade_carrinho.body["Len"]

    # selecionando todos os produtos cadastrados
    produtos = AdapterProduto(api_route=register_produto_composer(), data={})
    produtos = produtos.select_all()

    return render_template(
        "home.html",
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
    clientes = AdapterCliente(api_route=register_cliente_composer(), data={})
    clientes = clientes.select_all()

    # request do email e senhao do form
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")

        # comparando senha digitada com senha salva no banco
        for cliente in clientes.body:
            if cliente.email == email and senha == cliente.senha:
                apelido = cliente.apelido

                # coletando quantidade de produtos no carrinho de clientes
                quantidade_carrinho = AdapterCarrinho(
                    api_route=register_cliente_composer(), data={}
                )
                quantidade_carrinho = quantidade_carrinho.select_all()

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
            endereco = BuscarCep(
                api_route=buscar_cep_composer(), data={"cep_cliente": cep_cliente}
            )
            endereco = endereco.adapter_buscar_cep()
            endereco = endereco.body

            # se o usuario digitar algum complemento.
            if complemento:
                session["complemento"] = complemento
            else:
                session["complemento"] = endereco.complemento

        # comparação das senhas e retorna um valor boolean
        if senha and confirmar_senha:
            response_senha = validador_senha(senha, confirmar_senha)

            if not response_senha:
                flash("erro -- senhas não conferem !!")

            else:
                # registrar codigo no banco
                faker = Faker()
                codigo = faker.random_number(digits=4)
                enviar_codigobd = AdapterCodigo(
                    api_route=register_codigo_composer(),
                    data={"codigo": codigo, "id_cliente": 1},
                )
                enviar_codigobd.insert()

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

                return render_template(
                    "validacao_codigo.html", email=email, apelido=apelido
                )

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
            cliente_insert = AdapterCliente(
                api_route=register_cliente_composer(),
                data={
                    "apelido": cliente[1],
                    "email": cliente[2],
                    "senha": cliente[3],
                    "cep_cliente": cliente[4],
                },
            )
            response_cliente = cliente_insert.insert()

            id_cliente = response_cliente.body.id_cliente

            # salvando endereço no banco
            complemento = session.get("complemento")
            endereco = session.get("endereco_cliente")
            insert_endereco = AdapterEndereco(
                api_route=register_endereco_composer(),
                data={
                    "id_cliente": id_cliente,
                    "cep_cliente": endereco[0],
                    "estado": endereco[1],
                    "cidade": endereco[2],
                    "bairro": endereco[3],
                    "logradouro": endereco[4],
                    "complemento": complemento,
                },
            )
            insert_endereco.insert()

            # deletando do banco o codigo validado pelo cliente
            del_codigo = AdapterCodigo(
                api_route=register_codigo_composer(),
                data={"id_cliente": response_cliente.body.id_cliente},
            )
            del_codigo.delete()  # metodo para deletar o codigo no banco

            return redirect(
                url_for("api_routes.home", apelido=cliente[1], quantidade_carrinho=0)
            )

    return render_template("validacao_codigo.html", email=email)


@api_routes_bp.route(
    "/produtos/<apelido>/<quantidade_carrinho>/", methods=["GET", "POST"]
)
def produto(apelido: str, quantidade_carrinho: int):
    """endpoint para exibir produtos cadastrados"""

    select_produtos = AdapterProduto(api_route=register_produto_composer(), data={})
    select_produtos = select_produtos.select_all()

    return render_template(
        "produtos.html",
        apelido=apelido,
        quantidade_carrinho=quantidade_carrinho,
        produtos=select_produtos.body,
    )


@api_routes_bp.route(
    "/cadastrar_produto/<apelido>/<quantidade_carrinho>/", methods=["GET", "POST"]
)
def cadastrar_produto(apelido: str, quantidade_carrinho: int):
    """endpoint para cadastrar produtos"""

    if request.method == "POST":
        nome_produto = request.form.get("nome")
        descricao = request.form.get("descricao")
        preco = request.form.get("preco")
        # recebendo post do arquivo para upload
        imagem = request.files.get("upload")

        # adquirindo nome do arquivo do upload
        nome_imagem = imagem.filename

        # salvando arquivo na pasta static.
        diretorio = "C:\\meus projetos\\DeliverySystem\\CleanArchitecture\\src\\main\\configs\\static"
        imagem.save(os.path.join(diretorio, nome_imagem))

        # salvando os dados no banco
        cadastro_pro = AdapterProduto(
            api_route=register_produto_composer(),
            data={
                "nome": nome_produto,
                "descricao": descricao,
                "preco": float(preco),
                "imagem": nome_imagem,
            },
        )
        response = cadastro_pro.insert()
        if response.status_code == 200:
            return redirect(
                url_for(
                    "api_routes.cadastrar_produto",
                    apelido=apelido,
                    quantidade_carrinho=quantidade_carrinho,
                )
            )

    return render_template(
        "cadastrar_produto.html",
        apelido=apelido,
        quantidade_carrinho=quantidade_carrinho,
    )


@api_routes_bp.route(
    "/clientes/<apelido>/<quantidade_carrinho>", methods=["GET", "POST"]
)
def clientes(apelido: str, quantidade_carrinho: int):
    """Mostra na tela todos os clientes cadastrados."""
    # selecionando todos os clientes do banco
    clientes = AdapterCliente(api_route=register_cliente_composer(), data={})
    lista_clientes = clientes.select_all()
    # selecionando todos os endereços
    endereco = AdapterEndereco(api_route=register_endereco_composer(), data={})
    endereco = endereco.select_all()
    # verifica o status code da requisição
    if lista_clientes.status_code == 200 and endereco.status_code == 200:
        endereco = endereco.body
        lista_clientes = lista_clientes.body

    return render_template(
        "clientes.html",
        apelido=apelido,
        lista_clientes=lista_clientes,
        endereco=endereco,
        quantidade_carrinho=quantidade_carrinho,
    )


@api_routes_bp.route(
    "/deletar/<apelido>/<quantidade_carrinho>/<id_cliente>", methods=["GET", "POST"]
)
def deletar_cliente(apelido: str, quantidade_carrinho: int, id_cliente: int):
    """Endpoint para deletar clientes"""

    cliente = AdapterCliente(
        api_route=register_cliente_composer(), data={"id_cliente": int(id_cliente)}
    )
    endereco = AdapterEndereco(
        api_route=register_endereco_composer(), data={"id_cliente": int(id_cliente)}
    )
    cliente.delete()
    endereco.delete()

    return redirect(
        url_for(
            "api_routes.clientes",
            apelido=apelido,
            quantidade_carrinho=quantidade_carrinho,
        )
    )


@api_routes_bp.route(
    "/deletar_produto/<apelido>/<quantidade_carrinho>/<id_produto>",
    methods=["GET", "POST"],
)
def deletar_produto(apelido: str, quantidade_carrinho: int, id_produto: int):
    """Endpoint para deletar clientes"""

    produto = AdapterProduto(
        api_route=register_produto_composer(), data={"id_produto": int(id_produto)}
    )
    produto.delete()

    return redirect(
        url_for(
            "api_routes.produto",
            apelido=apelido,
            quantidade_carrinho=quantidade_carrinho,
        )
    )


@api_routes_bp.route(
    "/editar_produtos/<apelido>/<quantidade_carrinho>/<id_produto>",
    methods=["GET", "POST"],
)
def editar_produtos(apelido: str, quantidade_carrinho: int, id_produto: int):
    """editar produtos"""

    id_produto = int(id_produto)
    produtos = AdapterProduto(api_route=register_produto_composer(), data={})
    produtos = produtos.select_all()
    produtos = produtos.body

    if request.method == "POST":
        pass

    return render_template(
        "editar_produtos.html",
        id_produto=id_produto,
        apelido=apelido,
        produtos=produtos,
    )


@api_routes_bp.route("/sair/<apelido>", methods=["GET", "POST"])
def sair(apelido: str):
    """Função para encerrar o login. e o apelido passa a ser 'Efetue o login!'."""

    return redirect(url_for("api_routes.login", apelido="Efetue_o_Login!"))


@api_routes_bp.route("/testando/teste/denovo", methods=["GET", "POST"])
def nada():
    return render_template("teste.html")


@api_routes_bp.route("/buscando/api/post", methods=["GET", "POST"])
def buscar_api():
    return response.cep_cliente
