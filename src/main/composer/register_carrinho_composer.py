from src.main.interface.route_carrinho import RouteInterface
from src.presenters.controllers.register_carrinho_controller import (
    RegisterCarrinhoController,
)
from src.data.registrar_carrinho.registrar_carrinho import RegisterCarrinho
from src.infra.repo.carrinho_Repository import CarrinhoRepository


def register_carrinho_composer() -> RouteInterface:
    """Composing Register carrinho Route
    :param - None
    :return - Object with Register User Route
    """

    repository = CarrinhoRepository()
    use_case = RegisterCarrinho(repository)
    register_carrinho_route = RegisterCarrinhoController(use_case)

    return register_carrinho_route
