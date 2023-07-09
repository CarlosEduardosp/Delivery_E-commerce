from typing import Type, Dict

# from sqlalchemy.exc import IntegrityError
from src.main.interface.route_carrinho import RouteInterface as Route
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from src.presenters.errors.http_errors import HttpErrors


class AdapterCarrinho:
    """class carrinho adapter"""

    def __init__(self, api_route: Type[Route], data: Type[Dict]) -> any:
        self.api_route = api_route
        self.data = data

    def select_all(self):
        http_request = HttpRequest(query=self.data)
        response = self.api_route.route_select_all(http_request)

        return response

    def insert(self):
        query_data = self.data.keys()
        if "id_produto" and "id_cliente" in query_data:
            http_request = HttpRequest(query=self.data)
            response = self.api_route.route_insert(http_request)

            return response

        return self.__error()

    def select_len(self):
        query_data = self.data
        if "id_cliente" in query_data:
            http_request = HttpRequest(query=self.data)
            response = self.api_route.route_select(http_request)
            return response.body["Len"]

        return self.__error()

    def select(self):
        query_data = self.data.keys()
        if "id_cliente" in query_data:
            http_request = HttpRequest(query=self.data)
            response = self.api_route.route_select(http_request)

            return response

        return self.__error()

    def delete(self):
        query_data = self.data.keys()

        if "id_cliente" and "id_compra" in query_data:
            http_request = HttpRequest(query=self.data)
            response = self.api_route.route_delete(http_request)

            return response

        return self.__error()

    def __error(self):
        http_error = HttpErrors()
        return http_error.error_422()
