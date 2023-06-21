from typing import Type
from src.main.interface.route_codigo import RouteInterface
from src.doman.use_cases.register_codigo import RegisterCodigo
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from src.presenters.errors.http_errors import HttpErrors


class RegisterCodigoController(RouteInterface):
    """Class to define controller to register codigo use case"""

    def __init__(self, register_codigo_use_case: Type[RegisterCodigo]):
        self.register_codigo_use_case = register_codigo_use_case

    def route_insert(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.query:
            # If query

            query_string_params = (
                http_request.query.keys()
            )  # pega todas as chaves dentro de query

            if "id_cliente" in query_string_params and "codigo" in query_string_params:
                id_cliente = http_request.query["id_cliente"]
                codigo = http_request.query["codigo"]

                response = self.register_codigo_use_case.insert_codigo(
                    id_cliente=id_cliente, codigo=codigo
                )

            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

            return HttpResponse(status_code=200, body=response["Data"])

        # If no query in http_request
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    def route_select(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """controller select carrinho"""

        response = None
        data = http_request.query.keys()

        if "id_cliente" in data:
            id_cliente = http_request.query["id_cliente"]
            response = self.register_codigo_use_case.select_codigo(
                id_cliente=id_cliente
            )

        else:
            return {"Success": False, "Data": None}

        if response["Success"] is False:
            http_error = HttpErrors.error_422()
            return HttpResponse(
                status_code=http_error["status_code"], body=http_error["body"]
            )

        return HttpResponse(status_code=200, body=response["Data"])

    def route_delete(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """controller select carrinho"""

        response = None
        data = http_request.query.keys()

        if "id_cliente" in data:
            id_cliente = http_request.query["id_cliente"]
            response = self.register_codigo_use_case.delete_codigo(
                id_cliente=id_cliente
            )

        else:
            return {"Success": False, "Data": None}

        if response["Success"] is False:
            http_error = HttpErrors.error_422()
            return HttpResponse(
                status_code=http_error["status_code"], body=http_error["body"]
            )

        return HttpResponse(status_code=200, body=response["Data"])
