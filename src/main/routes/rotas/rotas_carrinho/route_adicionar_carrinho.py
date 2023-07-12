from src.main.routes.imports.imports_api_route import *  # noqa

api_routes_bp_adicionar_carrinho = Blueprint("rota_adicionar_carrinho", __name__)


@api_routes_bp_adicionar_carrinho.route(
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
        url_for("home.home", apelido=apelido, quantidade_carrinho=quantidade_carrinho)
    )
