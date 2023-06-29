from typing import Type, Dict

# from sqlalchemy.exc import IntegrityError
from src.main.interface.route_cliente import RouteInterface as Route
from src.presenters.helpers.http_models import HttpRequest, HttpResponse

# from src.presenters.errors.http_errors import HttpErrors
# from flask import request
# import json


def flask_adapter_cliente(
    api_route: Type[Route], data: Type[Dict], action: Type[str]
) -> any:
    """Adapter pattern to Flask
    :param - api_route - RouteInterface
    :param - data - dicionario com os dados da requisição
    :param - action - ação com as opções de string (insert, select, select_all, delete, update)
    :api_route: Composite Routes
    """

    # selecionando todos os clientes
    if action == "select_all":
        http_request = HttpRequest(query=data)
        response = api_route.route_select_all(http_request)

        return response

    # inserindo cliente no banco
    elif action == "insert":
        query_data = data.keys()

        if "apelido" and "email" and "senha" and "cep_cliente" in query_data:
            http_request = HttpRequest(query=data)
            response = api_route.route_insert(http_request)

            return response

    # selecionando um cliente especifico no banco
    elif action == "select":
        query_data = data.keys()

        if "id_cliente" in query_data:
            http_request = HttpRequest(query=data)
            response = api_route.route_select(http_request)

        return response

    # deletando um cliente especifico no banco
    elif action == "delete":
        query_data = data.keys()

        if "id_cliente" in query_data:
            http_request = HttpRequest(query=data)
            response = api_route.route_delete(http_request)

        return response

    # atualizando dados de cliente no banco
    elif action == "update":
        query_data = data.keys()

        if (
            "id_cliente"
            and "apelido"
            and "email"
            and "senha"
            and "cep_cliente" in query_data
        ):
            http_request = HttpRequest(query=data)
            response = api_route.route_update(http_request)

            return response

    return HttpResponse(status_code=200, body=None)
