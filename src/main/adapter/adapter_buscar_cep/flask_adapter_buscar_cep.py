from typing import Type, Dict

# from sqlalchemy.exc import IntegrityError
from src.main.interface.route_buscar_cep import RouteInterface as Route
from src.presenters.helpers.http_models import HttpRequest, HttpResponse

# from src.presenters.errors.http_errors import HttpErrors


def flask_adapter_buscar_cep(
    api_route: Type[Route], data: Type[Dict], action: Type[str]
) -> any:
    """Adapter pattern to Flask
    :param - api_route - RouteInterface
    :param - data - dicionario com os dados da requisição
    :param - action - ação com as opções de string ('cep_cliente')
    :api_route: Composite Routes
    """

    if action == "cep_cliente":
        http_request = HttpRequest(query=data)
        response = api_route.route_buscar_cep(http_request)
        return response.body

    else:
        return {"Success": False, "Data": None}
