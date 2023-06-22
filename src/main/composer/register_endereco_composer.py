from src.main.interface.route_endereco import RouteInterface
from src.presenters.controllers.register_endereco_controller import (
    RegisterEnderecoController,
)
from src.data.register_endereco.registrar_endereco import RegisterEndereco
from src.infra.repo.endereco_Repository import EnderecoRepository


def register_endereco_composer() -> RouteInterface:
    """Composing Register endereco Route
    :param - None
    :return - Object with Register User Route
    """

    repository = EnderecoRepository()
    use_case = RegisterEndereco(repository)
    register_endereco_route = RegisterEnderecoController(use_case)

    return register_endereco_route
