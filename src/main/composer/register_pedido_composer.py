from src.main.interface.route_pedido import RouteInterface
from src.presenters.controllers.register_pedido_controller import (
    RegisterPedidoController,
)
from src.data.registrar_pedido.registrar_pedido import RegisterPedido
from src.infra.repo.pedido_Repository import PedidoRepository


def register_pedido_composer() -> RouteInterface:
    """Composing Register pedido Route
    :param - None
    :return - Object with Register User Route
    """

    repository = PedidoRepository()
    use_case = RegisterPedido(repository)
    register_pedido_route = RegisterPedidoController(use_case)

    return register_pedido_route
