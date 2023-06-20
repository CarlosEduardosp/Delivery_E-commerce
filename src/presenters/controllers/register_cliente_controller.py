from typing import Type
from src.doman.use_cases.register_cliente import RegisterCliente
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from src.presenters.errors.http_errors import HttpErrors


class RegisterClienteController:
    """Class to define controller to register cliente use case"""

    def __init__(self, register_cliente_use_case: Type[RegisterCliente]):
        self.register_cliente_use_case = register_cliente_use_case

    def handle_insert(self, http_request: Type[HttpRequest]) -> HttpResponse:
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

    def handle_select(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """controller select cliente"""

        response = None
        data = http_request.query.keys()

        if "id_cliente" in data:
            id_cliente = http_request.query["id_cliente"]
            response = self.register_cliente_use_case.select_cliente(
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

    def handle_select_all(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """controller select cliente"""

        response = None

        response = self.register_cliente_use_case.select_all_cliente()

        return HttpResponse(status_code=200, body=response["Data"])

    def handle_delete(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """controller select cliente"""

        response = None
        data = http_request.query.keys()

        if "id_cliente" in data:
            id_cliente = http_request.query["id_cliente"]
            response = self.register_cliente_use_case.delete_cliente(
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

    def handle_update(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.query:
            # If query

            query_string_params = (
                http_request.query.keys()
            )  # pega todas as chaves dentro de query

            if (
                "id_cliente" in query_string_params
                and "apelido" in query_string_params
                and "email" in query_string_params
                and "senha" in query_string_params
                and "cep_cliente" in query_string_params
            ):
                id_cliente = http_request.query["id_cliente"]
                apelido = http_request.query["apelido"]
                email = http_request.query["email"]
                senha = http_request.query["senha"]
                cep_cliente = http_request.query["cep_cliente"]
                response = self.register_cliente_use_case.update_cliente(
                    id_cliente=id_cliente,
                    apelido=apelido,
                    email=email,
                    senha=senha,
                    cep_cliente=cep_cliente,
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
