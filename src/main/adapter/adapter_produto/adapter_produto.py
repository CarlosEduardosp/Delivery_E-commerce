from typing import Type, Dict

# from sqlalchemy.exc import IntegrityError
from src.main.interface.route_produto import RouteInterface as Route
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from src.presenters.errors.http_errors import HttpErrors


class AdapterProduto:
    """class produto adapter"""

    def __init__(self, api_route: Type[Route], data: Type[Dict]) -> any:
        self.api_route = api_route
        self.data = data
        self.query_data = data.keys()

    def select_all(self):
        http_request = HttpRequest(query=self.data)
        response = self.api_route.route_select_all(http_request)

        return response

    def insert(self):
        if "nome" and "descricao" and "imagem" and "preco" in self.query_data:
            http_request = HttpRequest(query=self.data)
            response = self.api_route.route_insert(http_request)

            return response

        return self.__error()

    def select(self):
        if "id_produto" in self.query_data:
            http_request = HttpRequest(query=self.data)
            response = self.api_route.route_select(http_request)

            return response

        return self.__error()

    def delete(self):
        if "id_produto" in self.query_data:
            http_request = HttpRequest(query=self.data)
            response = self.api_route.route_delete(http_request)

            return response

        return self.__error()

    def update(self):
        if (
            "id_produto"
            and "nome"
            and "descricao"
            and "imagem"
            and "preco" in self.query_data
        ):
            http_request = HttpRequest(query=self.data)
            response = self.api_route.route_update(http_request)

            return response

        return self.__error()

    def __error(self):
        http_error = HttpErrors()
        return http_error.error_422()
