from src.main.interface.route_cliente import RouteInterface
from src.presenters.controllers.register_cliente_controller import (
    RegisterClienteController,
)
from src.data.register_cliente.register_cliente import RegisterCliente
from src.infra.repo.cliente_Repository import ClienteRepository


def register_cliente_composer() -> RouteInterface:
    """Composing Register cliente Route
    :param - None
    :return - Object with Register User Route
    """

    repository = ClienteRepository()
    use_case = RegisterCliente(repository)
    register_cliente_route = RegisterClienteController(use_case)

    return register_cliente_route
