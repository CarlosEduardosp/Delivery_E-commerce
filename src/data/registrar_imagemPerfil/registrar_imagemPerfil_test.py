from faker import Faker
from .registrar_imagemperfil import RegisterImagemperfil
from src.infra.repo.imagemperfil_Repository import ImagemPerfilRepository

faker = Faker()


def test_register_imagem():
    """testing registry method"""

    user_repo = ImagemPerfilRepository()
    register_imagem = RegisterImagemperfil(user_repo)

    response = None

    try:
        response = register_imagem.insert_imagem(imagem=faker.name())
        return response
    except:
        return {"Success": False, "Data": response}

    return None


def test_select_imagem():
    """testing select imagem"""

    user_repo = ImagemPerfilRepository()
    register_imagem = RegisterImagemperfil(user_repo)

    response = None

    try:
        response = register_imagem.select_imagem()
        return response
    except:
        return response


def test_delete_imagem():
    """testing delete imagem"""

    user_repo = ImagemPerfilRepository()
    register_imagem = RegisterImagemperfil(user_repo)

    response = None
    try:
        response = register_imagem.delete_imagem()
        return response
    except:
        return response
