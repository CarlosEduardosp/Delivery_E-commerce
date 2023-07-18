from src.main.routes.imports.imports_api_route import *  # noqa

api_routes_bp_home = Blueprint("home", __name__)


@api_routes_bp_home.route(
    "/home/",
    methods=["GET", "POST"],
)
@api_routes_bp_home.route(
    "/home/<apelido>/<quantidade_carrinho>", methods=["GET", "POST"]
)
@api_routes_bp_home.route(
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

    # selecionar a imagem da tela principal no banco
    imagem = AdapterImagem(api_route=register_imagem_composer(), data={})
    imagem = imagem.select()

    if imagem.status_code == 200:
        imagem = imagem.body
        imagem = imagem.imagem
    else:
        imagem = ""

    return render_template(
        "home.html",
        apelido=apelido,
        quantidade_carrinho=quantidade_carrinho,
        produtos=produtos,
        imagem=imagem,
    )
