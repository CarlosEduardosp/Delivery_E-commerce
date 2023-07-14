from src.main.routes.imports.imports_api_route import *  # noqa

api_routes_bp_controle_pedido = Blueprint("rota_controle_pedido", __name__)


@api_routes_bp_controle_pedido.route(
    "/controle_pedido/<apelido>/<quantidade_carrinho>", methods=["GET", "POST"]
)
def controle_pedidos(apelido: str, quantidade_carrinho: int):
    """endpoint para controle de pedidos pelo adm"""

    cliente = AdapterCliente(api_route=register_cliente_composer(), data={})
    clientes = cliente.select_all()

    if clientes.status_code == 200:
        clientes = clientes.body

        lista_enderecos = []
        for cliente in clientes:
            endereco = AdapterEndereco(
                api_route=register_endereco_composer(),
                data={"id_cliente": cliente.id_cliente},
            )
            endereco = endereco.select()
            endereco = endereco.body

            dados = {"cliente": cliente, "endereco": endereco}

            lista_enderecos.append(dados)

            pedidos = AdapterPedido(
                api_route=register_pedido_composer(),
                data={},
            )
            pedidos = pedidos.select_all()
            if pedidos.status_code == 200:
                pedidos = pedidos.body

    produtos = AdapterProduto(api_route=register_produto_composer(), data={})
    produtos = produtos.select_all()
    produtos = produtos.body

    produtos_cliente = []
    lista_pedidos = []
    verificar = ""
    for pedido in pedidos:
        if verificar != pedido.numero_pedido:
            dados_pedido = {
                "numero_pedido": pedido.numero_pedido,
                "valor": pedido.valor,
                "id_cliente": pedido.id_cliente,
                "apelido": apelido,
                "status": pedido.status,
                "id_pedido": pedido.id_pedido,
                "data_pedido": pedido.data_pedido,
            }
            lista_pedidos.insert(0, dados_pedido)
        for x in produtos:
            if x.id_produto == pedido.id_produto:
                produtos_cliente.append(x)
            verificar = pedido.numero_pedido

    return render_template(
        "controle_pedido.html",
        apelido=apelido,
        quantidade_carrinho=quantidade_carrinho,
        produtos=produtos,
        pedidos=pedidos,
        lista_pedidos=lista_pedidos,
        produtos_cliente=produtos_cliente,
        lista_enderecos=lista_enderecos,
    )
