from src.main.interface.route_produto import RouteInterface
from src.presenters.controllers.register_produto_controller import (
    RegisterProdutoController,
)
from src.data.registrar_produto.register_produto import RegisterProduto
from src.infra.repo.produto_Repository import ProdutoRepository


def register_produto_composer() -> RouteInterface:
    """Composing Register produto Route
    :param - None
    :return - Object with Register User Route
    """

    repository = ProdutoRepository()
    use_case = RegisterProduto(repository)
    register_produto_route = RegisterProdutoController(use_case)

    return register_produto_route
