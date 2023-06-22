from src.main.interface.route_imagem import RouteInterface
from src.presenters.controllers.register_imagem_controller import (
    RegisterImagemController,
)
from src.data.registrar_imagemPerfil.registrar_imagemperfil import RegisterImagemperfil
from src.infra.repo.imagemperfil_Repository import ImagemPerfilRepository


def register_imagem_composer() -> RouteInterface:
    """Composing Register imagem Route
    :param - None
    :return - Object with Register User Route
    """

    repository = ImagemPerfilRepository()
    use_case = RegisterImagemperfil(repository)
    register_imagem_route = RegisterImagemController(use_case)

    return register_imagem_route
