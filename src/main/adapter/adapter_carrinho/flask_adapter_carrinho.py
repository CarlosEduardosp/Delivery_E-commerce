from typing import Type, Dict

# from sqlalchemy.exc import IntegrityError
from src.main.interface.route_carrinho import RouteInterface as Route
from src.presenters.helpers.http_models import HttpRequest, HttpResponse

# from src.presenters.errors.http_errors import HttpErrors


def flask_adapter_carrinho(
    api_route: Type[Route], data: Type[Dict], action: Type[str]
) -> any:
    """Adapter pattern to Flask
    :param - api_route - RouteInterface
    :param - data - dicionario com os dados da requisição
    :param - action - ação com as opções de string (insert, select, select_all, select_len, delete, update)
    :api_route: Composite Routes
    """

    # selecionando todos os carrinhos
    if action == "select_all":
        http_request = HttpRequest(query=data)
        response = api_route.route_select_all(http_request)

        return response.body["Dados"]

    # inserindo carrinho no banco
    elif action == "insert":
        query_data = data.keys()

        if "id_produto" and "id_cliente" in query_data:
            http_request = HttpRequest(query=data)
            response = api_route.route_insert(http_request)

            return response

    # selecionando um carrinho especifico no banco
    elif action == "select_len":
        query_data = data.keys()

        if "id_cliente" in query_data:
            http_request = HttpRequest(query=data)
            response = api_route.route_select(http_request)
            return response.body["Len"]
        else:
            return "Vazio"

        return response

    elif action == "select":
        query_data = data.keys()

        if "id_cliente" in query_data:
            http_request = HttpRequest(query=data)
            response = api_route.route_select(http_request)

        return response.body["Dados"]

    # deletando um carrinho especifico no banco
    elif action == "delete":
        query_data = data.keys()

        if "id_cliente" and "id_produto" in query_data:
            http_request = HttpRequest(query=data)
            response = api_route.route_delete(http_request)

        return response
