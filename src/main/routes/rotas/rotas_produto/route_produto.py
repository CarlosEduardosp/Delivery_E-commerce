from src.main.routes.imports.imports_api_route import *  # noqa

api_routes_bp_produto = Blueprint("rota_produto", __name__)


@api_routes_bp_produto.route(
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
