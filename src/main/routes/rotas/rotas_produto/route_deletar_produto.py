from src.main.routes.imports.imports_api_route import *  # noqa

api_routes_bp_del_produto = Blueprint("deletar_produto", __name__)


@api_routes_bp_del_produto.route(
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
