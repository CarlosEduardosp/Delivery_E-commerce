from faker import Faker
from src.data.registrar_carrinho.registrar_carrinho import RegisterCarrinho
from src.infra.repo.carrinho_Repository import CarrinhoRepository
from src.presenters.helpers.http_models import HttpRequest
from .register_carrinho_controller import RegisterCarrinhoController


faker = Faker()


def handle():
    """Testing Handle method"""

    register_carrinho_use_case = RegisterCarrinho(CarrinhoRepository())
    register_carrinho_controller = RegisterCarrinhoController(
        register_carrinho_use_case
    )

    http_request = HttpRequest(
        query={
            "id_cliente": faker.random_number(digits=1),
            "id_produto": faker.random_number(digits=1),
        }
    )

    response = register_carrinho_controller.route_insert(http_request)

    return response


def select_controller():
    """testing controller select"""

    register_carrinho_use_case = RegisterCarrinho(CarrinhoRepository())
    register_carrinho_controller = RegisterCarrinhoController(
        register_carrinho_use_case
    )

    http_request = HttpRequest(query={"id_cliente": faker.random_number(digits=1)})

    response = register_carrinho_controller.route_select(http_request)

    return response


def select_all_controller():
    """testing select all"""

    register_carrinho_use_case = RegisterCarrinho(CarrinhoRepository())
    register_carrinho_controller = RegisterCarrinhoController(
        register_carrinho_use_case
    )

    http_request = HttpRequest()
    response = register_carrinho_controller.route_select_all(http_request)

    return response


def delete_controller():
    """testing controller delete"""

    register_carrinho_use_case = RegisterCarrinho(CarrinhoRepository())
    register_carrinho_controller = RegisterCarrinhoController(
        register_carrinho_use_case
    )

    http_request = HttpRequest(query={"id_cliente": 1, "id_compra": 2})

    response = register_carrinho_controller.route_delete(http_request)

    return response
