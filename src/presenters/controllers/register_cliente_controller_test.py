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

    response = register_cliente_controller.handle(http_request)

    return response
