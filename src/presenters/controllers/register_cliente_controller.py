from typing import Type
from src.doman.use_cases.register_cliente import RegisterCliente
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from src.presenters.errors.http_errors import HttpErrors


class RegisterClienteController:
    """Class to define controller to register cliente use case"""

    def __init__(self, register_cliente_use_case: Type[RegisterCliente]):
        self.register_cliente_use_case = register_cliente_use_case

    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.query:
            # If query

            query_string_params = (
                http_request.query.keys()
            )  # pega todas as chaves dentro de query

            if (
                "apelido" in query_string_params
                and "email" in query_string_params
                and "senha" in query_string_params
                and "cep_cliente" in query_string_params
            ):
                apelido = http_request.query["apelido"]
                email = http_request.query["email"]
                senha = http_request.query["senha"]
                cep_cliente = http_request.query["cep_cliente"]
                response = self.register_cliente_use_case.register(
                    apelido=apelido, email=email, senha=senha, cep_cliente=cep_cliente
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
