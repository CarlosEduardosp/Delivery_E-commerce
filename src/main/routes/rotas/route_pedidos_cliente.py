from src.main.routes.imports.imports_api_route import *  # noqa

api_routes_bp_pedidos_cliente = Blueprint("rota_pedidos_cliente", __name__)


@api_routes_bp_pedidos_cliente.route(
    "/meus_pedidos/<apelido>/<quantidade_carrinho>/", methods=["GET", "POST"]
)
def pedidos_cliente(apelido: str, quantidade_carrinho: int):
    """exibe todos os pedidos para o usuário"""

    cliente = AdapterCliente(
        api_route=register_cliente_composer(), data={"apelido": apelido}
    )
    cliente = cliente.select()
    cliente = cliente.body[0]

    pedidos = AdapterPedido(
        api_route=register_pedido_composer(), data={"id_cliente": cliente.id_cliente}
    )
    pedidos = pedidos.select()
    pedidos = pedidos.body

    produtos = AdapterProduto(api_route=register_produto_composer(), data={})
    produtos = produtos.select_all()
    produtos = produtos.body

    produtos_cliente = []
    lista_pedidos = []
    verificar = ""
    for pedido in pedidos:
        if pedido.id_cliente == cliente.id_cliente:
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
        "pedidos_cliente.html",
        apelido=apelido,
        quantidade_carrinho=quantidade_carrinho,
        produtos=produtos,
        pedidos=pedidos,
        lista_pedidos=lista_pedidos,
        produtos_cliente=produtos_cliente,
    )
