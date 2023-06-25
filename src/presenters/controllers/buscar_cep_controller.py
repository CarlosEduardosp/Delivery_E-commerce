from typing import Type
from src.main.interface.route_buscar_cep import RouteInterface
from src.doman.use_cases.buscar_cep import BuscarCepInterface
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from src.presenters.errors.http_errors import HttpErrors


class BuscarCepController(RouteInterface):
    """Class to define controller to register carrinho use case"""

    def __init__(self, buscar_cep_use_case: Type[BuscarCepInterface]):
        self.buscar_cep_use_case = buscar_cep_use_case

    def route_buscar_cep(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.query:
            # If query

            query_string_params = (
                http_request.query.keys()
            )  # pega todas as chaves dentro de query

            if "cep_cliente" in query_string_params:
                cep_cliente = http_request.query["cep_cliente"]

                response = self.buscar_cep_use_case.pesquisar_cep(
                    cep_cliente=cep_cliente
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
