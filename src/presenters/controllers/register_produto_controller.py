from typing import Type
from src.doman.use_cases.register_produto import RegisterProduto
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from src.presenters.errors.http_errors import HttpErrors


class RegisterProdutoController:
    """Class to define controller to register produto use case"""

    def __init__(self, register_produto_use_case: Type[RegisterProduto]):
        self.register_produto_use_case = register_produto_use_case

    def handle_insert(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.query:
            # If query

            query_string_params = (
                http_request.query.keys()
            )  # pega todas as chaves dentro de query

            if (
                "nome" in query_string_params
                and "descricao" in query_string_params
                and "imagem" in query_string_params
                and "preco" in query_string_params
            ):
                nome = http_request.query["nome"]
                descricao = http_request.query["descricao"]
                imagem = http_request.query["imagem"]
                preco = http_request.query["preco"]
                response = self.register_produto_use_case.register(
                    nome=nome, descricao=descricao, imagem=imagem, preco=preco
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
        """controller select produto"""

        response = None
        data = http_request.query.keys()

        if "id_produto" in data:
            id_produto = http_request.query["id_produto"]
            response = self.register_produto_use_case.select_produto(
                id_produto=id_produto
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

        response = self.register_produto_use_case.select_all_produto()

        return HttpResponse(status_code=200, body=response["Data"])

    def handle_delete(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """controller select produto"""

        response = None
        data = http_request.query.keys()

        if "id_produto" in data:
            id_produto = http_request.query["id_produto"]
            response = self.register_produto_use_case.delete_produto(
                id_produto=id_produto
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
                "id_produto" in query_string_params
                and "nome" in query_string_params
                and "descricao" in query_string_params
                and "imagem" in query_string_params
                and "preco" in query_string_params
            ):
                id_produto = http_request.query["id_produto"]
                nome = http_request.query["nome"]
                descricao = http_request.query["descricao"]
                imagem = http_request.query["imagem"]
                preco = http_request.query["preco"]
                response = self.register_produto_use_case.update_produto(
                    id_produto=id_produto,
                    nome=nome,
                    descricao=descricao,
                    imagem=imagem,
                    preco=preco,
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
