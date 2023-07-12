from src.main.routes.imports.imports_api_route import *  # noqa

api_routes_bp_del_carrinho = Blueprint("rota_deletar_carrinho", __name__)


@api_routes_bp_del_carrinho.route(
    "/deletar_carrinho/<apelido>/<quantidade_carrinho>/<id_produto>",
    methods=["GET", "POST"],
)
def deletar_carrinho(apelido: str, quantidade_carrinho: int, id_produto: int):
    """Endpoint para deletar produtos no carrinho"""

    # buscando cliente no banco de dados com apelido
    cliente = AdapterCliente(
        api_route=register_cliente_composer(), data={"apelido": apelido}
    )
    cliente = cliente.select()
    cliente = cliente.body[0]

    # selecionando todos os produtos no carrinho
    carrinho = AdapterCarrinho(api_route=register_carrinho_composer(), data={})
    carrinho = carrinho.select_all()

    if apelido == cliente.apelido:
        for i in carrinho.body:
            # comparando o id_produto enviado com o selecionando no carrinho
            if i.id_produto == int(id_produto):
                carrinho = AdapterCarrinho(
                    api_route=register_carrinho_composer(),
                    data={
                        "id_compra": int(i.id_compra),
                        "id_cliente": cliente.id_cliente,
                    },
                )
                carrinho.delete()

                # diminui um item do numeros total de produtos no carrinho.
                quantidade_carrinho = int(quantidade_carrinho)
                if quantidade_carrinho > 0:
                    quantidade_carrinho = quantidade_carrinho - 1
                break

    return redirect(
        url_for(
            "rota_carrinho.carrinho",
            apelido=apelido,
            quantidade_carrinho=quantidade_carrinho,
        )
    )
