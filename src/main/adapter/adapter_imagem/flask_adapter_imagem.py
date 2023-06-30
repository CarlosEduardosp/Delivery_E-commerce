from typing import Type, Dict

# from sqlalchemy.exc import IntegrityError
from src.main.interface.route_imagem import RouteInterface as Route
from src.presenters.helpers.http_models import HttpRequest, HttpResponse

# from src.presenters.errors.http_errors import HttpErrors


def flask_adapter_imagem(
    api_route: Type[Route], data: Type[Dict], action: Type[str]
) -> any:
    """Adapter pattern to Flask
    :param - api_route - RouteInterface
    :param - data - dicionario com os dados da requisição
    :param - action - ação com as opções de string (insert, select, select_all, delete, update)
    :api_route: Composite Routes
    """

    # inserindo imagem no banco
    if action == "insert":
        query_data = data.keys()

        if "imagem" in query_data:
            http_request = HttpRequest(query=data)
            response = api_route.route_insert(http_request)

            return response

    # selecionando uma imagem específica no banco
    elif action == "select":
        http_request = HttpRequest()
        response = api_route.route_select(http_request)

        return response

    # deletando uma imagem específica no banco
    elif action == "delete":
        http_request = HttpRequest()
        response = api_route.route_delete(http_request)

        return response
