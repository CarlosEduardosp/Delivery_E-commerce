from faker import Faker
from src.data.registrar_codigo.registrar_codigo import RegisterCodigo
from src.infra.repo.codigo_Repository import CodigoRepository
from src.presenters.helpers.http_models import HttpRequest
from .register_codigo_controller import RegisterCodigoController


faker = Faker()


def test_handle():
    """Testing Handle method"""

    register_codigo_use_case = RegisterCodigo(CodigoRepository())
    register_codigo_controller = RegisterCodigoController(register_codigo_use_case)

    http_request = HttpRequest(
        query={
            "id_cliente": faker.random_number(digits=1),
            "codigo": faker.random_number(digits=3),
        }
    )

    response = register_codigo_controller.route_insert(http_request)

    return response


def test_select_controller():
    """testing controller select"""

    register_codigo_use_case = RegisterCodigo(CodigoRepository())
    register_codigo_controller = RegisterCodigoController(register_codigo_use_case)

    http_request = HttpRequest(query={"id_cliente": faker.random_number(digits=1)})

    response = register_codigo_controller.route_select(http_request)

    return response


def test_delete_controller():
    """testing controller delete"""

    register_codigo_use_case = RegisterCodigo(CodigoRepository())
    register_codigo_controller = RegisterCodigoController(register_codigo_use_case)

    http_request = HttpRequest(query={"id_cliente": 1})

    response = register_codigo_controller.route_delete(http_request)

    return response
