from .imports_api_route import *  # noqa

api_routes_bp = Blueprint("api_routes", __name__)


@api_routes_bp.route(
    "/home/",
    methods=["GET", "POST"],
)
@api_routes_bp.route("/home/<apelido>/<quantidade_carrinho>", methods=["GET", "POST"])
@api_routes_bp.route(
    "/home/<apelido>/<quantidade_carrinho>/",
    defaults={"apelido": "Efetue_o_Login!", "quantidade_carrinho": "Vazio"},
    methods=["GET", "POST"],
)
def home(apelido: str, quantidade_carrinho: int):
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
    "/efetuar_login/<apelido>/<quantidade_carrinho>", methods=["GET", "POST"]
)
def login(apelido: str, quantidade_carrinho: int):
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
                # coletando quantidade de produtos no carrinho de clientes
                quantidade_carrinho = AdapterCarrinho(
                    api_route=register_carrinho_composer(),
                    data={"id_cliente": cliente.id_cliente},
                )
                quantidade_carrinho = quantidade_carrinho.select()
                # selecionando a quantidade de itens no carrinho dentro do "Len"
                quantidade_carrinho = quantidade_carrinho.body["Len"]

                apelido = cliente.apelido

                return redirect(
                    url_for(
                        "api_routes.home",
                        apelido=apelido,
                        quantidade_carrinho=quantidade_carrinho,
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
        if codigo:
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

                apelido = cliente[1]

                return redirect(
                    url_for("api_routes.home", apelido=apelido, quantidade_carrinho=0)
                )

    return render_template(
        "validacao_codigo.html", email=email, apelido="Efetue_o_Login!"
    )


@api_routes_bp.route(
    "/produtos/<apelido>/<quantidade_carrinho>/", methods=["GET", "POST"]
)
def produto(apelido: str, quantidade_carrinho: int):
    """endpoint para exibir produtos cadastrados"""

    # seleciona todos os produtos
    select_produtos = AdapterProduto(api_route=register_produto_composer(), data={})
    select_produtos = select_produtos.select_all()
    produtos = select_produtos.body

    return render_template(
        "produtos.html",
        apelido=apelido,
        quantidade_carrinho=quantidade_carrinho,
        produtos=produtos,
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
        diretorio = "./src/main/configs/static/"
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
    "/carrinho/<apelido>/<quantidade_carrinho>", methods=["GET", "POST"]
)
def carrinho(apelido: str, quantidade_carrinho: int):
    """carrinho de compras"""

    # seleciona cliente atraves do apelido
    cliente = AdapterCliente(
        api_route=register_cliente_composer(), data={"apelido": apelido}
    )
    cliente = cliente.select()
    cliente = cliente.body[0]

    # seleciona todos os produtos
    produto = AdapterProduto(api_route=register_produto_composer(), data={})
    produto = produto.select_all()
    produtos = produto.body

    # seleciona os itens no carrinho com id cliente igual cliente.id_cliente
    carrinho = AdapterCarrinho(
        api_route=register_carrinho_composer(), data={"id_cliente": cliente.id_cliente}
    )
    carrinho = carrinho.select()

    # seleciona os dados dos produtos que estçao no carrinho
    produtos_no_carrinho = []
    for i in produtos:
        for j in carrinho.body["Dados"]:
            if i.id_produto == j.id_produto:
                produtos_no_carrinho.append(i)

    return render_template(
        "carrinho.html",
        apelido=apelido,
        quantidade_carrinho=quantidade_carrinho,
        produtos_no_carrinho=produtos_no_carrinho,
    )


@api_routes_bp.route(
    "/adicionar_carrinho/<apelido>/<quantidade_carrinho>/<id_produto>",
    methods=["GET", "POST"],
)
def adicionar_carrinho(apelido: str, quantidade_carrinho: int, id_produto: int):
    """adiciona produtos ao carrinho"""

    # seleciona todos os clientes
    cliente = AdapterCliente(api_route=register_cliente_composer(), data={})
    clientes = cliente.select_all()

    # adiciona produto ao carrinho de clientes.(adiciona id_cliente e o id_produto)
    for i in clientes.body:
        if apelido == i.apelido:
            id_cliente = i.id_cliente
            carrinho = AdapterCarrinho(
                api_route=register_carrinho_composer(),
                data={"id_cliente": int(id_cliente), "id_produto": int(id_produto)},
            )
            carrinho.insert()

    return redirect(
        url_for(
            "api_routes.home", apelido=apelido, quantidade_carrinho=quantidade_carrinho
        )
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
    # cria a instancia do cliente para deletar
    cliente = AdapterCliente(
        api_route=register_cliente_composer(), data={"id_cliente": int(id_cliente)}
    )
    # cria a instancia do endereço para deletar
    endereco = AdapterEndereco(
        api_route=register_endereco_composer(), data={"id_cliente": int(id_cliente)}
    )
    # deletando endereço e cliente
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

    # fazendo a requisição do nome da imagem do produto
    nome_imagem = AdapterProduto(
        api_route=register_produto_composer(), data={"id_produto": int(id_produto)}
    )
    nome_imagem = nome_imagem.select()
    nome_imagem = nome_imagem.body.imagem

    # deletando a imagem da pasta static
    # path = f"C:\\meus projetos\\DeliverySystem\\CleanArchitecture\\src\\main\\configs\\static\\{nome_imagem}"
    path = f"./src/main/configs/static/{nome_imagem}"
    os.remove(path)

    # deletando o produto do banco de dados
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
    "/deletar_carrinho/<apelido>/<quantidade_carrinho>/<id_produto>",
    methods=["GET", "POST"],
)
def deletar_carrinho(apelido: str, quantidade_carrinho: int, id_produto: int):
    """Endpoint para deletar produtos no carrinho"""

    # buscando cliente no banco de dados com apelido
    cliente = AdapterCliente(
        api_route=register_cliente_composer(), data={"apelido": apelido}
    )
    cliente = cliente.select()
    cliente = cliente.body[0]

    # selecionando todos os produtos no carrinho
    carrinho = AdapterCarrinho(api_route=register_carrinho_composer(), data={})
    carrinho = carrinho.select_all()

    if apelido == cliente.apelido:
        for i in carrinho.body:
            # comparando o id_produto enviado com o selecionando no carrinho
            if i.id_produto == int(id_produto):
                carrinho = AdapterCarrinho(
                    api_route=register_carrinho_composer(),
                    data={
                        "id_compra": int(i.id_compra),
                        "id_cliente": cliente.id_cliente,
                    },
                )
                carrinho.delete()

                # diminui um item do numeros total de produtos no carrinho.
                quantidade_carrinho = int(quantidade_carrinho)
                if quantidade_carrinho > 0:
                    quantidade_carrinho = quantidade_carrinho - 1
                break

    return redirect(
        url_for(
            "api_routes.carrinho",
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

    # seleciona todos os produtos com a função select_all
    id_produto = int(id_produto)
    produtos = AdapterProduto(api_route=register_produto_composer(), data={})
    produtos = produtos.select_all()
    produtos = produtos.body

    # faz o request dos dados passados por formulario
    if request.method == "POST":
        nome = request.form.get("nome")
        descricao = request.form.get("descricao")
        preco = float(request.form.get("preco"))

        # faz o upadate dos produtos com os dados passados por formulário
        for i in produtos:
            if id_produto == i.id_produto:
                todos_produtos = AdapterProduto(
                    api_route=register_produto_composer(),
                    data={
                        "id_produto": id_produto,
                        "nome": nome,
                        "descricao": descricao,
                        "preco": preco,
                        "imagem": i.imagem,
                    },
                )
                todos_produtos.update()

                return redirect(
                    url_for(
                        "api_routes.produto",
                        apelido=apelido,
                        quantidade_carrinho=quantidade_carrinho,
                    )
                )

    return render_template(
        "editar_produtos.html",
        id_produto=id_produto,
        apelido=apelido,
        produtos=produtos,
        quantidade_carrinho=quantidade_carrinho,
    )


@api_routes_bp.route("/perfil/<apelido>/<quantidade_carrinho>", methods=["GET", "POST"])
def perfil(apelido: str, quantidade_carrinho: int):
    """Perfil com os dados do cliente ou administrador"""

    # seleciona todos os clientes e endereços
    cliente = AdapterCliente(api_route=register_cliente_composer(), data={})
    clientes = cliente.select_all()
    endereco = AdapterEndereco(api_route=register_endereco_composer(), data={})
    endereco_cliente = endereco.select_all()

    # faz o request dos dados passados via formulário
    if request.method == "POST":
        email = request.form.get("email")
        apelido_request = request.form.get("apelido")
        cep_cliente = request.form.get("cep_cliente")
        estado = request.form.get("estado")
        cidade = request.form.get("cidade")
        bairro = request.form.get("bairro")
        logradouro = request.form.get("logradouro")
        complemento = request.form.get("complemento")

        # verifica se todos os campos foram preenchidos
        if (
            email
            and apelido_request
            and cep_cliente
            and estado
            and cidade
            and bairro
            and logradouro
            and complemento
        ):
            # compara o cliente com a lista de clientes e em seguida realiza o update
            for i in clientes.body:
                if apelido == i.apelido:
                    cliente = AdapterCliente(
                        api_route=register_cliente_composer(),
                        data={
                            "id_cliente": i.id_cliente,
                            "apelido": apelido_request,
                            "email": email,
                            "senha": i.senha,
                            "cep_cliente": cep_cliente,
                        },
                    )
                    cliente.update()

                #  realiza o update do endereço do cliente selecionado
                for x in endereco_cliente.body:
                    if i.id_cliente == x.id_cliente:
                        endereco = AdapterEndereco(
                            api_route=register_endereco_composer(),
                            data={
                                "id_endereco": x.id_endereco,
                                "cep_cliente": cep_cliente,
                                "estado": estado,
                                "cidade": cidade,
                                "bairro": bairro,
                                "logradouro": logradouro,
                                "complemento": complemento,
                                "id_cliente": i.id_cliente,
                            },
                        )
                        endereco.update()

            # envia uma msg de confirmação do update
            mensagem = f"{apelido}, Seus Dados Foram Alterados com Sucesso."
            flash(mensagem)
            return redirect(
                url_for(
                    "api_routes.perfil",
                    apelido=apelido_request,
                    quantidade_carrinho=quantidade_carrinho,
                )
            )
    # salva o conteudo dentro do Body para enviar ao template perfil.html
    clientes = cliente.select_all()
    clientes = clientes.body
    endereco = endereco.select_all()
    endereco = endereco.body

    return render_template(
        "perfil.html",
        apelido=apelido,
        quantidade_carrinho=quantidade_carrinho,
        clientes=clientes,
        endereco=endereco,
    )


@api_routes_bp.route("/pedido/<apelido>/<quantidade_carrinho>", methods=["GET", "POST"])
def pedido(apelido: str, quantidade_carrinho: int):
    """Mostra os detalhes do pedido, como produtos e especificações, dados do cliente, e também os valores"""

    # selecionando o cliente
    cliente = AdapterCliente(
        api_route=register_cliente_composer(), data={"apelido": apelido}
    )
    cliente = cliente.select()
    cliente = cliente.body[0]

    # selecionando o endereço do cliente
    endereco = AdapterEndereco(
        api_route=register_endereco_composer(), data={"id_cliente": cliente.id_cliente}
    )
    endereco = endereco.select()
    endereco = endereco.body

    # selecionando os produtos no carrinho do cliente
    carrinho = AdapterCarrinho(api_route=register_carrinho_composer(), data={})
    carrinho = carrinho.select_all()
    carrinho = carrinho.body

    # selecionando todos os produtos
    produtos = AdapterProduto(api_route=register_produto_composer(), data={})
    produtos = produtos.select_all()
    produtos = produtos.body

    # selecionando as informações dos produtos que estão no carrinho do cliente.
    produtos_no_carrinho = []
    valor = 0
    for i in carrinho:
        for j in produtos:
            if i.id_produto == j.id_produto:
                produtos_no_carrinho.append(j)
                valor = valor + j.preco

    # formatando o valor para 2 casas decimais
    valor = f"{valor:,.2f}"
    valor = float(valor)

    return render_template(
        "pedido.html",
        apelido=apelido,
        quantidade_carrinho=quantidade_carrinho,
        cliente=cliente,
        endereco=endereco,
        produtos_no_carrinho=produtos_no_carrinho,
        valor=valor,
    )


@api_routes_bp.route("/sair/<apelido>/<quantidade_carrinho>", methods=["GET", "POST"])
def sair(apelido: str, quantidade_carrinho: str):
    """Função para encerrar o login. e o apelido passa a ser 'Efetue o login!'."""

    return redirect(
        url_for(
            "api_routes.login", apelido="Efetue_o_Login!", quantidade_carrinho=int(0)
        )
    )
