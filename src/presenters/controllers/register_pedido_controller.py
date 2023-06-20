from typing import Type
from src.doman.use_cases.register_pedido import RegisterPedido
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from src.presenters.errors.http_errors import HttpErrors


class RegisterPedidoController:
    """Class to define controller to register pedido use case"""

    def __init__(self, register_pedido_use_case: Type[RegisterPedido]):
        self.register_pedido_use_case = register_pedido_use_case

    def handle_insert(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.query:
            # If query

            query_string_params = (
                http_request.query.keys()
            )  # pega todas as chaves dentro de query

            if (
                "id_cliente" in query_string_params
                and "id_produto" in query_string_params
                and "numero_pedido" in query_string_params
                and "valor" in query_string_params
                and "data_pedido" in query_string_params
                and "status" in query_string_params
            ):
                id_cliente = http_request.query["id_cliente"]
                id_produto = http_request.query["id_produto"]
                numero_pedido = http_request.query["numero_pedido"]
                valor = http_request.query["valor"]
                data_pedido = http_request.query["data_pedido"]
                status = http_request.query["status"]
                response = self.register_pedido_use_case.insert_pedido(
                    id_cliente=id_cliente,
                    id_produto=id_produto,
                    numero_pedido=numero_pedido,
                    valor=valor,
                    data_pedido=data_pedido,
                    status=status,
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

        if "id_cliente" in data and "id_pedido" in data:
            id_cliente = http_request.query["id_cliente"]
            id_pedido = http_request.query["id_pedido"]
            response = self.register_pedido_use_case.select_pedido(
                id_cliente=id_cliente, id_pedido=id_pedido
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

        response = self.register_pedido_use_case.select_all_pedido()

        return HttpResponse(status_code=200, body=response["Data"])

    def handle_delete(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """controller select pedido"""

        response = None
        data = http_request.query.keys()

        if "id_pedido" in data and "id_cliente" in data:
            id_pedido = http_request.query["id_pedido"]
            id_cliente = http_request.query["id_cliente"]

            response = self.register_pedido_use_case.delete_pedido(
                id_pedido=id_pedido, id_cliente=id_cliente
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
                "id_pedido" in query_string_params
                and "id_cliente" in query_string_params
                and "id_produto" in query_string_params
                and "numero_pedido" in query_string_params
                and "valor" in query_string_params
                and "data_pedido" in query_string_params
                and "status" in query_string_params
            ):
                id_pedido = http_request.query["id_pedido"]
                id_cliente = http_request.query["id_cliente"]
                id_produto = http_request.query["id_produto"]
                numero_pedido = http_request.query["numero_pedido"]
                valor = http_request.query["valor"]
                data_pedido = http_request.query["data_pedido"]
                status = http_request.query["status"]

                response = self.register_pedido_use_case.update_pedido(
                    id_pedido=id_pedido,
                    id_cliente=id_cliente,
                    id_produto=id_produto,
                    numero_pedido=numero_pedido,
                    valor=valor,
                    data_pedido=data_pedido,
                    status=status,
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
