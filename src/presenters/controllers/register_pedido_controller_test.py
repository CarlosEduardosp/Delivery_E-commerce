from faker import Faker
from src.data.registrar_pedido.registrar_pedido import RegisterPedido
from src.infra.repo.pedido_Repository import PedidoRepository
from src.presenters.helpers.http_models import HttpRequest
from .register_pedido_controller import RegisterPedidoController


faker = Faker()


def test_handle():
    """Testing Handle method"""

    register_pedido_use_case = RegisterPedido(PedidoRepository())
    register_pedido_controller = RegisterPedidoController(register_pedido_use_case)

    http_request = HttpRequest(
        query={
            "id_cliente": faker.random_number(digits=1),
            "id_produto": faker.random_number(digits=1),
            "numero_pedido": faker.random_number(digits=1),
            "valor": float(faker.random_number(digits=2)),
            "data_pedido": faker.name(),
            "status": faker.name(),
        }
    )

    response = register_pedido_controller.handle_insert(http_request)

    return response


def test_select_controller():
    """testing controller select"""

    register_pedido_use_case = RegisterPedido(PedidoRepository())
    register_pedido_controller = RegisterPedidoController(register_pedido_use_case)

    http_request = HttpRequest(
        query={
            "id_cliente": faker.random_number(digits=1),
            "id_pedido": faker.random_number(digits=1),
        }
    )

    response = register_pedido_controller.handle_select(http_request)

    return response


def test_select_all_controller():
    """testing select all"""

    register_pedido_use_case = RegisterPedido(PedidoRepository())
    register_pedido_controller = RegisterPedidoController(register_pedido_use_case)

    http_request = HttpRequest()
    response = register_pedido_controller.handle_select_all(http_request)

    return response


def test_delete_controller():
    """testing controller delete"""

    register_pedido_use_case = RegisterPedido(PedidoRepository())
    register_pedido_controller = RegisterPedidoController(register_pedido_use_case)

    http_request = HttpRequest(query={"id_cliente": 0, "id_pedido": 3})

    response = register_pedido_controller.handle_delete(http_request)

    return response


def test_handle_update():
    """Testing Handle method"""

    register_pedido_use_case = RegisterPedido(PedidoRepository())
    register_pedido_controller = RegisterPedidoController(register_pedido_use_case)

    http_request = HttpRequest(
        query={
            "id_pedido": 1,
            "id_cliente": faker.random_number(digits=1),
            "id_produto": faker.random_number(digits=1),
            "numero_pedido": faker.random_number(digits=1),
            "valor": float(faker.random_number(digits=2)),
            "data_pedido": faker.name(),
            "status": faker.name(),
        }
    )

    response = register_pedido_controller.handle_update(http_request)

    return response
