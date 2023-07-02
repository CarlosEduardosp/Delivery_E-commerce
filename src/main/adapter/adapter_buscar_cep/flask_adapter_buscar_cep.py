from typing import Type, Dict

# from sqlalchemy.exc import IntegrityError
from src.main.interface.route_buscar_cep import RouteInterface as Route
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from src.presenters.errors.http_errors import HttpErrors

# from src.presenters.errors.http_errors import HttpErrors
from src.main.interface_adapter.buscarCepInterface import BuscarCepInterface


class BuscarCep(BuscarCepInterface):
    def __init__(self, api_route: type[Route], data: Type[Dict]):
        self.api_route = api_route
        self.data = data

    def adapter_buscar_cep(self) -> any:
        """class adapter buscar cep"""

        try:
            if self.data:
                http_request = HttpRequest(query=self.data)
                response = self.api_route.route_buscar_cep(http_request)

                return response

            else:
                return {"Success": False, "Data": None}

        except:
            http_error = HttpErrors()
            return http_error.error_422()
