from typing import Type, Dict

# from sqlalchemy.exc import IntegrityError
from src.main.interface.route_imagem import RouteInterface as Route
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from src.presenters.errors.http_errors import HttpErrors


class AdapterImagem:
    """class Imagem adapter"""

    def __init__(self, api_route: Type[Route], data: Type[Dict]) -> any:
        self.api_route = api_route
        self.data = data
        self.query_data = data.keys()

    def insert(self):
        if "imagem" in self.query_data:
            http_request = HttpRequest(query=self.data)
            response = self.api_route.route_insert(http_request)

            return response

        http_error = HttpErrors.error_422()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    def select(self):
        try:
            http_request = HttpRequest(query=self.data)
            response = self.api_route.route_select(http_request)

            return response

        except:
            http_error = HttpErrors.error_422()
            return HttpResponse(
                status_code=http_error["status_code"], body=http_error["body"]
            )

    def delete(self):
        try:
            http_request = HttpRequest(query=self.data)
            response = self.api_route.route_delete(http_request)

            return response

        except:
            return self.__error()

    def __error(self):
        http_error = HttpErrors()
        return http_error.error_422()
