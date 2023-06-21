from typing import Type
from src.main.interface.route_endereco import RouteInterface
from src.doman.use_cases.register_endereco import RegisterEndereco
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from src.presenters.errors.http_errors import HttpErrors


class RegisterEnderecoController(RouteInterface):
    """Class to define controller to register endereco use case"""

    def __init__(self, register_endereco_use_case: Type[RegisterEndereco]):
        self.register_endereco_use_case = register_endereco_use_case

    def route_insert(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.query:
            # If query

            query_string_params = (
                http_request.query.keys()
            )  # pega todas as chaves dentro de query

            if (
                "cep_cliente" in query_string_params
                and "estado" in query_string_params
                and "cidade" in query_string_params
                and "bairro" in query_string_params
                and "logradouro" in query_string_params
                and "complemento" in query_string_params
                and "id_cliente" in query_string_params
            ):
                cep_cliente = http_request.query["cep_cliente"]
                estado = http_request.query["estado"]
                cidade = http_request.query["cidade"]
                bairro = http_request.query["bairro"]
                logradouro = http_request.query["logradouro"]
                complemento = http_request.query["complemento"]
                id_cliente = http_request.query["id_cliente"]
                response = self.register_endereco_use_case.insert_endereco(
                    cep_cliente=cep_cliente,
                    estado=estado,
                    cidade=cidade,
                    bairro=bairro,
                    logradouro=logradouro,
                    complemento=complemento,
                    id_cliente=id_cliente,
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
        """controller select produto"""

        response = None
        data = http_request.query.keys()

        if "id_cliente" in data:
            id_cliente = http_request.query["id_cliente"]
            response = self.register_endereco_use_case.select_endereco(
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

    def route_select_all(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """controller select cliente"""

        response = None

        response = self.register_endereco_use_case.select_all_endereco()

        return HttpResponse(status_code=200, body=response["Data"])

    def route_delete(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """controller select produto"""

        response = None
        data = http_request.query.keys()

        if "id_cliente" in data:
            id_cliente = http_request.query["id_cliente"]
            response = self.register_endereco_use_case.delete_endereco(
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

    def route_update(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.query:
            # If query

            query_string_params = (
                http_request.query.keys()
            )  # pega todas as chaves dentro de query

            if (
                "id_endereco" in query_string_params
                and "cep_cliente" in query_string_params
                and "estado" in query_string_params
                and "cidade" in query_string_params
                and "bairro" in query_string_params
                and "logradouro" in query_string_params
                and "complemento" in query_string_params
                and "id_cliente" in query_string_params
            ):
                id_endereco = http_request.query["id_endereco"]
                cep_cliente = http_request.query["cep_cliente"]
                estado = http_request.query["estado"]
                cidade = http_request.query["cidade"]
                bairro = http_request.query["bairro"]
                logradouro = http_request.query["logradouro"]
                complemento = http_request.query["complemento"]
                id_cliente = http_request.query["id_cliente"]
                response = self.register_endereco_use_case.update_endereco(
                    id_endereco=id_endereco,
                    cep_cliente=cep_cliente,
                    estado=estado,
                    cidade=cidade,
                    bairro=bairro,
                    logradouro=logradouro,
                    complemento=complemento,
                    id_cliente=id_cliente,
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
