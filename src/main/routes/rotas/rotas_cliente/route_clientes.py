from src.main.routes.imports.imports_api_route import *  # noqa

api_routes_bp_clientes = Blueprint("rota_clientes", __name__)


@api_routes_bp_clientes.route(
    "/clientes/<apelido>/<quantidade_carrinho>", methods=["GET", "POST"]
)
def clientes(apelido: str, quantidade_carrinho: int):
    """Mostra na tela todos os clientes cadastrados."""

    # selecionando todos os clientes do banco
    clientes = AdapterCliente(api_route=register_cliente_composer(), data={})
    lista_clientes = clientes.select_all()

    # selecionando todos os endereços
    endereco = AdapterEndereco(api_route=register_endereco_composer(), data={})
    endereco = endereco.select_all()

    # verifica o status code da requisição
    if lista_clientes.status_code == 200 and endereco.status_code == 200:
        endereco = endereco.body
        lista_clientes = lista_clientes.body

    return render_template(
        "clientes.html",
        apelido=apelido,
        lista_clientes=lista_clientes,
        endereco=endereco,
        quantidade_carrinho=quantidade_carrinho,
    )
