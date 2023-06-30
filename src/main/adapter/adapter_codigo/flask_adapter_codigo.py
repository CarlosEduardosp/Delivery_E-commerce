from typing import Type, Dict

# from sqlalchemy.exc import IntegrityError
from src.main.interface.route_codigo import RouteInterface as Route
from src.presenters.helpers.http_models import HttpRequest, HttpResponse

# from src.presenters.errors.http_errors import HttpErrors


def flask_adapter_codigo(
    api_route: Type[Route], data: Type[Dict], action: Type[str]
) -> any:
    """Adapter pattern to Flask
    :param - api_route - RouteInterface
    :param - data - dicionario com os dados da requisição
    :param - action - ação com as opções de string (insert, select, select_all, delete, update)
    :api_route: Composite Routes
    """

    # inserindo codigo no banco
    if action == "insert":
        query_data = data.keys()

        if "codigo" in query_data:
            http_request = HttpRequest(query=data)
            response = api_route.route_insert(http_request)

            return response

    # selecionando um codigo especifico no banco
    elif action == "select":
        query_data = data.keys()

        if "id_cliente" in query_data:
            http_request = HttpRequest(query=data)
            response = api_route.route_select(http_request)

        return response

    # deletando um codigo especifico no banco
    elif action == "delete":
        query_data = data.keys()
        response = None

        if "id_cliente" in query_data:
            http_request = HttpRequest(query=data)
            response = api_route.route_delete(http_request)

        return response
