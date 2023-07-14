from src.main.routes.imports.imports_api_route import *  # noqa

api_routes_bp_atualizar_status_pedido = Blueprint(
    "rota_atualizar_status_pedido", __name__
)


@api_routes_bp_atualizar_status_pedido.route(
    "/atualizar_status_pedido/<apelido>/<quantidade_carrinho>/<numero_pedido>/<id_cliente>",
    methods=["GET", "POST"],
)
def atualizar_status_pedido(
    apelido: str, quantidade_carrinho: int, numero_pedido: int, id_cliente: int
):
    """endpoint para atualizar status de pedidos pelo adm"""

    if request.method == "POST":
        resposta_atualizacao = request.form.get("radio1")

        if resposta_atualizacao:
            pedido = AdapterPedido(
                api_route=register_pedido_composer(), data={"id_cliente": id_cliente}
            )
            pedido = pedido.select()
            if pedido.status_code == 200:
                pedido = pedido.body

                numero_pedido = int(numero_pedido)
                for i in pedido:
                    if i.numero_pedido == numero_pedido:
                        update = AdapterPedido(
                            api_route=register_pedido_composer(),
                            data={
                                "id_pedido": i.id_pedido,
                                "id_cliente": i.id_cliente,
                                "id_produto": i.id_produto,
                                "numero_pedido": i.numero_pedido,
                                "valor": i.valor,
                                "data_pedido": i.data_pedido,
                                "status": resposta_atualizacao,
                            },
                        )
                        update.update()

                    # chamar método que envia um email com o novo status do pedido

    return redirect(
        url_for(
            "rota_controle_pedido.controle_pedidos",
            apelido=apelido,
            quantidade_carrinho=quantidade_carrinho,
        )
    )
