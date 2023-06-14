from faker import Faker
from .registrar_codigo import RegisterCodigo
from src.infra.repo.codigo_Repository import CodigoRepository

faker = Faker()


def test_register_codigo():
    """testing registry method"""

    user_repo = CodigoRepository()
    register_codigo = RegisterCodigo(user_repo)

    response = None

    try:
        response = register_codigo.insert_codigo(
            codigo=faker.random_number(digits=3),
            id_cliente=faker.random_number(digits=1),
        )
        return response
    except:
        return {"Success": False, "Data": response}

    return None


def test_select_carrinho():
    """testing select codigo"""

    user_repo = CodigoRepository()
    register_codigo = RegisterCodigo(user_repo)

    response = None

    try:
        response = register_codigo.select_codigo(id_cliente=9)
        return response
    except:
        return response


def test_delete_carrinho():
    """testing delete codigo"""

    user_repo = CodigoRepository()
    register_codigo = RegisterCodigo(user_repo)

    response = None
    try:
        response = register_codigo.delete_codigo(
            id_cliente=faker.random_number(digits=1)
        )
        return response
    except:
        return response
