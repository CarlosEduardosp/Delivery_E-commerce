from typing import Type, Dict

# from sqlalchemy.exc import IntegrityError
from src.main.interface.route_pedido import RouteInterface as Route
from src.presenters.helpers.http_models import HttpRequest, HttpResponse

# from src.presenters.errors.http_errors import HttpErrors


def flask_adapter_pedido(
    api_route: Type[Route], data: Type[Dict], action: Type[str]
) -> any:
    """Adapter pattern to Flask
    :param - api_route - RouteInterface
    :param - data - dicionario com os dados da requisição
    :param - action - ação com as opções de string (insert, select, select_all, delete, update)
    :api_route: Composite Routes
    """

    # selecionando todos os pedidos
    if action == "select_all":
        http_request = HttpRequest(query=data)
        response = api_route.route_select_all(http_request)

        return response

    # inserindo pedido no banco
    elif action == "insert":
        query_data = data.keys()

        if (
            "id_cliente"
            and "id_produto"
            and "numero_pedido"
            and "valor"
            and "data_pedido"
            and "status" in query_data
        ):
            http_request = HttpRequest(query=data)
            response = api_route.route_insert(http_request)

            return response

    # selecionando um pedido especifico no banco
    elif action == "select":
        query_data = data.keys()

        if "id_cliente" and "id_pedido" in query_data:
            http_request = HttpRequest(query=data)
            response = api_route.route_select(http_request)

        return response

    # deletando um pedido especifico no banco
    elif action == "delete":
        query_data = data.keys()

        if "id_cliente" and "id_pedido" in query_data:
            http_request = HttpRequest(query=data)
            response = api_route.route_delete(http_request)

        return response

    # atualizando dados de pedido no banco
    elif action == "update":
        query_data = data.keys()

        if (
            "id_pedido"
            and "id_cliente"
            and "id_produto"
            and "numero_pedido"
            and "valor"
            and "data_pedido"
            and "status" in query_data
        ):
            http_request = HttpRequest(query=data)
            response = api_route.route_update(http_request)

            return response

    return HttpResponse(status_code=200, body=None)
