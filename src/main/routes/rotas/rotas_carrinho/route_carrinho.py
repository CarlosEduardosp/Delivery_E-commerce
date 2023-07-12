from src.main.routes.imports.imports_api_route import *  # noqa

api_routes_bp_carrinho = Blueprint("rota_carrinho", __name__)


@api_routes_bp_carrinho.route(
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
