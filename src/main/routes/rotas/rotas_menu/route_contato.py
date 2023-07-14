from src.main.routes.imports.imports_api_route import *  # noqa

api_routes_bp_contato = Blueprint("rota_contato", __name__)


@api_routes_bp_contato.route(
    "/contato/<apelido>/<quantidade_carrinho>", methods=["GET", "POST"]
)
def contato(apelido: str, quantidade_carrinho: int):
    """contato do desenvolvedor"""

    return render_template(
        "contato.html", apelido=apelido, quantidade_carrinho=quantidade_carrinho
    )
