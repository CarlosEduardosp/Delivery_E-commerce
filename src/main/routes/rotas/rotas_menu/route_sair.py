from src.main.routes.imports.imports_api_route import *  # noqa

api_routes_bp_sair = Blueprint("rota_sair", __name__)


@api_routes_bp_sair.route(
    "/sair/<apelido>/<quantidade_carrinho>", methods=["GET", "POST"]
)
def sair(apelido: str, quantidade_carrinho: str):
    """Função para encerrar o login. e o apelido passa a ser 'Efetue o login!'."""

    return redirect(
        url_for(
            "rota_login.login", apelido="Efetue_o_Login!", quantidade_carrinho=int(0)
        )
    )
