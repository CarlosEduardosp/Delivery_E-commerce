from src.main.routes.imports.imports_api_route import *  # noqa

api_routes_bp = Blueprint("api_routes", __name__)


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
            "rota_clientes.clientes",
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
            "rota_produto.produto",
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
            "rota_carrinho.carrinho",
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
                        "rota_produto.produto",
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


@api_routes_bp.route(
    "/confirmar_pedido/<apelido>/<quantidade_carrinho>/<valor>", methods=["GET", "POST"]
)
def confirmar_pedido(apelido: str, quantidade_carrinho: int, valor: float):
    """exibe os dados do pedido para o usuário"""

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

    # recebendo a data atual
    data_pedido = date.today().strftime("%d/%m/%Y")

    # selecionando todos os produtos
    produtos = AdapterProduto(api_route=register_produto_composer(), data={})
    produtos = produtos.select_all()
    produtos = produtos.body

    # selecionando as informações dos produtos que estão no carrinho do cliente.
    produtos_no_carrinho = []
    for i in carrinho:
        for j in produtos:
            if i.id_produto == j.id_produto:
                produtos_no_carrinho.append(j)

    # adicionando o numero de pedido
    numero_pedido = AdapterPedido(api_route=register_pedido_composer(), data={})
    numero_pedido = numero_pedido.select_all()
    numero_pedido = numero_pedido.body

    # se somando 1 ao numero do ultimo pedido, para o novo pedido.
    if not numero_pedido:
        numero_pedido = int(1)
    else:
        numero_pedido = numero_pedido[-1].numero_pedido + int(1)

    for i in carrinho:
        pedido = AdapterPedido(
            api_route=register_pedido_composer(),
            data={
                "id_cliente": cliente.id_cliente,
                "id_produto": i.id_produto,
                "numero_pedido": int(numero_pedido),
                "valor": float(valor),
                "data_pedido": str(data_pedido),
                "status": "Preparando",
            },
        )
        pedido = pedido.insert()
        pedido = pedido.body

        deletar_carrinho = AdapterCarrinho(
            api_route=register_carrinho_composer(),
            data={"id_compra": i.id_compra, "id_cliente": i.id_cliente},
        )
        deletar_carrinho.delete()

        # zerando o carrinho do cliente no template
        quantidade_carrinho = int(0)

    return render_template(
        "confirmar_pedido.html",
        apelido=apelido,
        quantidade_carrinho=quantidade_carrinho,
        endereco=endereco,
        dados_do_pedido=pedido,
        cliente=cliente,
        produtos_no_carrinho=produtos_no_carrinho,
        valor=valor,
    )


@api_routes_bp.route("/sair/<apelido>/<quantidade_carrinho>", methods=["GET", "POST"])
def sair(apelido: str, quantidade_carrinho: str):
    """Função para encerrar o login. e o apelido passa a ser 'Efetue o login!'."""

    return redirect(
        url_for(
            "rota_login.login", apelido="Efetue_o_Login!", quantidade_carrinho=int(0)
        )
    )
