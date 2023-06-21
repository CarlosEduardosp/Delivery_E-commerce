from faker import Faker
from src.data.registrar_imagemPerfil.registrar_imagemperfil import RegisterImagemperfil
from src.infra.repo.imagemperfil_Repository import ImagemPerfilRepository
from src.presenters.helpers.http_models import HttpRequest
from .register_imagem_controller import RegisterImagemController


faker = Faker()


def test_handle():
    """Testing Handle method"""

    register_imagem_use_case = RegisterImagemperfil(ImagemPerfilRepository())
    register_imagem_controller = RegisterImagemController(register_imagem_use_case)

    http_request = HttpRequest(query={"imagem": faker.name()})

    response = register_imagem_controller.handle_insert(http_request)

    return response


def test_select_controller():
    """testing controller select"""

    register_imagem_use_case = RegisterImagemperfil(ImagemPerfilRepository())
    register_imagem_controller = RegisterImagemController(register_imagem_use_case)

    http_request = HttpRequest()

    response = register_imagem_controller.handle_select(http_request)

    return response


def test_delete_controller():
    """testing controller delete"""

    register_imagem_use_case = RegisterImagemperfil(ImagemPerfilRepository())
    register_imagem_controller = RegisterImagemController(register_imagem_use_case)

    http_request = HttpRequest()

    response = register_imagem_controller.handle_delete(http_request)

    return response
