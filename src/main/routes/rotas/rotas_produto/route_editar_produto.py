from src.main.routes.imports.imports_api_route import *  # noqa

api_routes_bp_editar_produto = Blueprint("rota_editar_produto", __name__)


@api_routes_bp_editar_produto.route(
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
