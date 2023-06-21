from typing import Type
from src.doman.use_cases.register_imagemperfil import RegisterImagem
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from src.presenters.errors.http_errors import HttpErrors


class RegisterImagemController:
    """Class to define controller to register imagem use case"""

    def __init__(self, register_imagem_use_case: Type[RegisterImagem]):
        self.register_imagem_use_case = register_imagem_use_case

    def handle_insert(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.query:
            # If query

            query_string_params = (
                http_request.query.keys()
            )  # pega todas as chaves dentro de query

            if "imagem" in query_string_params:
                imagem = http_request.query["imagem"]

                response = self.register_imagem_use_case.insert_imagem(imagem=imagem)

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

        response = self.register_imagem_use_case.select_imagem()

        if response["Success"] is False:
            http_error = HttpErrors.error_422()
            return HttpResponse(
                status_code=http_error["status_code"], body=http_error["body"]
            )

        return HttpResponse(status_code=200, body=response["Data"])

    def handle_delete(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """controller select carrinho"""

        response = None

        response = self.register_imagem_use_case.delete_imagem()

        if response["Success"] is False:
            http_error = HttpErrors.error_422()
            return HttpResponse(
                status_code=http_error["status_code"], body=http_error["body"]
            )

        return HttpResponse(status_code=200, body=response["Data"])
