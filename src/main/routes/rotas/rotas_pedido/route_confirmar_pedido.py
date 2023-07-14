from src.main.routes.imports.imports_api_route import *  # noqa

api_routes_bp_confirmar_pedido = Blueprint("rota_confirmar_pedido", __name__)


@api_routes_bp_confirmar_pedido.route(
    "/confirmar_pedido/<apelido>/<quantidade_carrinho>/<valor>", methods=["GET", "POST"]
)
def confirmar_pedido(apelido: str, quantidade_carrinho: int, valor: float):
    """exibe os dados do pedido para o usuário"""

    # selecionando o cliente
    cliente = AdapterCliente(
        api_route=register_cliente_composer(), data={"apelido": apelido}
    )
    cliente = cliente.select()
    if cliente.status_code == 200:
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
