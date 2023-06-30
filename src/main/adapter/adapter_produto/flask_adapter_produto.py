from typing import Type, Dict

# from sqlalchemy.exc import IntegrityError
from src.main.interface.route_produto import RouteInterface as Route
from src.presenters.helpers.http_models import HttpRequest, HttpResponse

# from src.presenters.errors.http_errors import HttpErrors


def flask_adapter_produto(
    api_route: Type[Route], data: Type[Dict], action: Type[str]
) -> any:
    """Adapter pattern to Flask
    :param - api_route - RouteInterface
    :param - data - dicionario com os dados da requisição
    :param - action - ação com as opções de string (insert, select, select_all, delete, update)
    :api_route: Composite Routes
    """

    # selecionando todos os produto
    if action == "select_all":
        http_request = HttpRequest(query=data)
        response = api_route.route_select_all(http_request)

        return response

    # inserindo produto no banco
    elif action == "insert":
        query_data = data.keys()

        if "nome" and "descricao" and "imagem" and "preco" in query_data:
            http_request = HttpRequest(query=data)
            response = api_route.route_insert(http_request)

            return response

    # selecionando um produto especifico no banco
    elif action == "select":
        query_data = data.keys()

        if "id_produto" in query_data:
            http_request = HttpRequest(query=data)
            response = api_route.route_select(http_request)

        return response

    # deletando um produto especifico no banco
    elif action == "delete":
        query_data = data.keys()

        if "id_produto" in query_data:
            http_request = HttpRequest(query=data)
            response = api_route.route_delete(http_request)

        return response

    # atualizando dados de produto no banco
    elif action == "update":
        query_data = data.keys()

        if (
            "id_produto"
            and "nome"
            and "descricao"
            and "imagem"
            and "preco" in query_data
        ):
            http_request = HttpRequest(query=data)
            response = api_route.route_update(http_request)

            return response

    return HttpResponse(status_code=200, body=None)
