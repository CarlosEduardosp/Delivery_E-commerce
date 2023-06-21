from faker import Faker
from src.data.register_cliente.register_cliente import RegisterCliente
from src.infra.repo.cliente_Repository import ClienteRepository
from src.presenters.helpers.http_models import HttpRequest
from .register_cliente_controller import RegisterClienteController


faker = Faker()


def test_handle():
    """Testing Handle method"""

    register_cliente_use_case = RegisterCliente(ClienteRepository())
    register_cliente_controller = RegisterClienteController(register_cliente_use_case)

    http_request = HttpRequest(
        query={
            "apelido": faker.name(),
            "email": faker.email(),
            "senha": faker.name(),
            "cep_cliente": faker.name(),
        }
    )

    response = register_cliente_controller.route_insert(http_request)

    return response


def test_select_controller():
    """testing controller select"""

    register_cliente_use_case = RegisterCliente(ClienteRepository())
    register_cliente_controller = RegisterClienteController(register_cliente_use_case)

    http_request = HttpRequest(query={"id_cliente": faker.random_number(digits=1)})

    response = register_cliente_controller.route_select(http_request)

    return response


def test_select_all_controller():
    """testing select all"""

    register_cliente_use_case = RegisterCliente(ClienteRepository())
    register_cliente_controller = RegisterClienteController(register_cliente_use_case)

    http_request = HttpRequest()
    response = register_cliente_controller.route_select_all(http_request)

    return response


def test_delete_controller():
    """testing controller delete"""

    register_cliente_use_case = RegisterCliente(ClienteRepository())
    register_cliente_controller = RegisterClienteController(register_cliente_use_case)

    http_request = HttpRequest(query={"id_cliente": faker.random_number(digits=2)})

    response = register_cliente_controller.route_delete(http_request)

    return response


def test_handle_update():
    """Testing Handle method"""

    register_cliente_use_case = RegisterCliente(ClienteRepository())
    register_cliente_controller = RegisterClienteController(register_cliente_use_case)

    http_request = HttpRequest(
        query={
            "id_cliente": 10,
            "apelido": faker.name(),
            "email": faker.email(),
            "senha": faker.name(),
            "cep_cliente": faker.name(),
        }
    )

    response = register_cliente_controller.route_update(http_request)

    return response
