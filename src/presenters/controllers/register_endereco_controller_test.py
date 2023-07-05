from faker import Faker
from src.data.register_endereco.registrar_endereco import RegisterEndereco
from src.infra.repo.endereco_Repository import EnderecoRepository
from src.presenters.helpers.http_models import HttpRequest
from .register_endereco_controller import RegisterEnderecoController


faker = Faker()


def test_handle():
    """Testing Handle method"""

    register_endereco_use_case = RegisterEndereco(EnderecoRepository())
    register_endereco_controller = RegisterEnderecoController(
        register_endereco_use_case
    )

    http_request = HttpRequest(
        query={
            "cep_cliente": str(faker.random_number(digits=8)),
            "estado": faker.name(),
            "cidade": faker.name(),
            "bairro": faker.name(),
            "logradouro": faker.name(),
            "complemento": faker.name(),
            "id_cliente": faker.random_number(digits=2),
        }
    )

    response = register_endereco_controller.route_insert(http_request)

    return response


def select_controller():
    """testing controller select"""

    register_endereco_use_case = RegisterEndereco(EnderecoRepository())
    register_endereco_controller = RegisterEnderecoController(
        register_endereco_use_case
    )

    http_request = HttpRequest(query={"id_cliente": faker.random_number(digits=1)})

    response = register_endereco_controller.route_select(http_request)

    return response


def test_select_all_controller():
    """testing select all"""

    register_endereco_use_case = RegisterEndereco(EnderecoRepository())
    register_endereco_controller = RegisterEnderecoController(
        register_endereco_use_case
    )

    http_request = HttpRequest()
    response = register_endereco_controller.route_select_all(http_request)

    return response


def test_delete_controller():
    """testing controller delete"""

    register_endereco_use_case = RegisterEndereco(EnderecoRepository())
    register_endereco_controller = RegisterEnderecoController(
        register_endereco_use_case
    )

    http_request = HttpRequest(query={"id_cliente": faker.random_number(digits=2)})

    response = register_endereco_controller.route_delete(http_request)

    return response


def test_handle_update():
    """Testing Handle method"""

    register_endereco_use_case = RegisterEndereco(EnderecoRepository())
    register_endereco_controller = RegisterEnderecoController(
        register_endereco_use_case
    )

    http_request = HttpRequest(
        query={
            "id_endereco": 1,
            "cep_cliente": str(faker.random_number(digits=8)),
            "estado": faker.name(),
            "cidade": faker.name(),
            "bairro": faker.name(),
            "logradouro": faker.name(),
            "complemento": faker.name(),
            "id_cliente": 9,
        }
    )

    response = register_endereco_controller.route_update(http_request)

    return response
