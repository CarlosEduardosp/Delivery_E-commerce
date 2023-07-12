from src.main.routes.imports.imports_api_route import *  # noqa

api_routes_bp_pedido = Blueprint("rota_pedido", __name__)


@api_routes_bp_pedido.route(
    "/pedido/<apelido>/<quantidade_carrinho>", methods=["GET", "POST"]
)
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
