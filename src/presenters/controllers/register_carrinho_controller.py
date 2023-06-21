from typing import Type
from src.doman.use_cases.register_carrinho import RegisterCarrinho
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from src.presenters.errors.http_errors import HttpErrors


class RegisterCarrinhoController:
    """Class to define controller to register carrinho use case"""

    def __init__(self, register_carrinho_use_case: Type[RegisterCarrinho]):
        self.register_carrinho_use_case = register_carrinho_use_case

    def handle_insert(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.query:
            # If query

            query_string_params = (
                http_request.query.keys()
            )  # pega todas as chaves dentro de query

            if (
                "id_produto" in query_string_params
                and "id_cliente" in query_string_params
            ):
                id_produto = http_request.query["id_produto"]
                id_cliente = http_request.query["id_cliente"]

                response = self.register_carrinho_use_case.insert_carrinho(
                    id_produto=id_produto, id_cliente=id_cliente
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
        """controller select carrinho"""

        response = None
        data = http_request.query.keys()

        if "id_cliente" in data:
            id_cliente = http_request.query["id_cliente"]
            response = self.register_carrinho_use_case.select_carrinho(
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

        response = self.register_carrinho_use_case.select_all_carrinho()

        return HttpResponse(status_code=200, body=response["Data"])

    def handle_delete(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """controller select carrinho"""

        response = None
        data = http_request.query.keys()

        if "id_cliente" in data and "id_produto" in data:
            id_cliente = http_request.query["id_cliente"]
            id_produto = http_request.query["id_produto"]
            response = self.register_carrinho_use_case.delete_carrinho(
                id_cliente=id_cliente, id_produto=id_produto
            )

        else:
            return {"Success": False, "Data": None}

        if response["Success"] is False:
            http_error = HttpErrors.error_422()
            return HttpResponse(
                status_code=http_error["status_code"], body=http_error["body"]
            )

        return HttpResponse(status_code=200, body=response["Data"])
