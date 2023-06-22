from src.main.interface.route_codigo import RouteInterface
from src.presenters.controllers.register_codigo_controller import (
    RegisterCodigoController,
)
from src.data.registrar_codigo.registrar_codigo import RegisterCodigo
from src.infra.repo.codigo_Repository import CodigoRepository


def register_codigo_composer() -> RouteInterface:
    """Composing Register codigo Route
    :param - None
    :return - Object with Register User Route
    """

    repository = CodigoRepository()
    use_case = RegisterCodigo(repository)
    register_codigo_route = RegisterCodigoController(use_case)

    return register_codigo_route
