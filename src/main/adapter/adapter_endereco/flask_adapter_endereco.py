from typing import Type, Dict

# from sqlalchemy.exc import IntegrityError
from src.main.interface.route_endereco import RouteInterface as Route
from src.presenters.helpers.http_models import HttpRequest, HttpResponse

# from src.presenters.errors.http_errors import HttpErrors


def flask_adapter_endereco(
    api_route: Type[Route], data: Type[Dict], action: Type[str]
) -> any:
    """Adapter pattern to Flask
    :param - api_route - RouteInterface
    :param - data - dicionario com os dados da requisição
    :param - action - ação com as opções de string (insert, select, select_all, delete, update)
    :api_route: Composite Routes
    """

    # selecionando todos os endereços
    if action == "select_all":
        http_request = HttpRequest(query=data)
        response = api_route.route_select_all(http_request)

        return response

    # inserindo endereço no banco
    elif action == "insert":
        query_data = data.keys()

        if (
            "cep_cliente"
            and "estado"
            and "cidade"
            and "bairro"
            and "logradouro"
            and "complemento"
            and "id_cliente" in query_data
        ):
            http_request = HttpRequest(query=data)
            response = api_route.route_insert(http_request)

            return response

    # selecionando um endereço especifico no banco
    elif action == "select":
        query_data = data.keys()

        if "id_cliente" in query_data:
            http_request = HttpRequest(query=data)
            response = api_route.route_select(http_request)

        return response

    # deletando um endereço especifico no banco
    elif action == "delete":
        query_data = data.keys()

        if "id_cliente" in query_data:
            http_request = HttpRequest(query=data)
            response = api_route.route_delete(http_request)

        return response

    # atualizando dados de endereço no banco
    elif action == "update":
        query_data = data.keys()

        if (
            "id_endereco"
            and "cep-cliente"
            and "estado"
            and "cidade"
            and "bairro"
            and "logradouro"
            and "complemento"
            and "id_cliente" in query_data
        ):
            http_request = HttpRequest(query=data)
            response = api_route.route_update(http_request)

            return response

    return HttpResponse(status_code=200, body=None)
