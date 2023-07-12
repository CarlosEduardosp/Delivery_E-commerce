from src.main.routes.imports.imports_api_route import *  # noqa

api_routes_bp_del_cliente = Blueprint("deletar_cliente", __name__)


@api_routes_bp_del_cliente.route(
    "/deletar/<apelido>/<quantidade_carrinho>/<id_cliente>", methods=["GET", "POST"]
)
def deletar_cliente(apelido: str, quantidade_carrinho: int, id_cliente: int):
    """Endpoint para deletar clientes"""
    # cria a instancia do cliente para deletar
    cliente = AdapterCliente(
        api_route=register_cliente_composer(), data={"id_cliente": int(id_cliente)}
    )
    # cria a instancia do endereço para deletar
    endereco = AdapterEndereco(
        api_route=register_endereco_composer(), data={"id_cliente": int(id_cliente)}
    )
    # deletando endereço e cliente
    cliente.delete()
    endereco.delete()

    return redirect(
        url_for(
            "rota_clientes.clientes",
            apelido=apelido,
            quantidade_carrinho=quantidade_carrinho,
        )
    )
