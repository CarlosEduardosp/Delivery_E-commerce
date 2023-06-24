from faker import Faker
from .registrar_endereco import RegisterEndereco
from src.infra.repo.endereco_Repository import EnderecoRepository

faker = Faker()


def test_insert_endereco():
    """testing endereco"""

    user_repo = EnderecoRepository()
    register_endereco = RegisterEndereco(user_repo)

    response = None
    try:
        response = register_endereco.insert_endereco(
            cep_cliente=faker.name(),
            estado=faker.name(),
            cidade=faker.name(),
            bairro=faker.name(),
            logradouro=faker.name(),
            complemento=faker.name(),
            id_cliente=faker.random_number(digits=1),
        )
        return response
    except:
        return {"Success": False, "Data": response}


def test_select_endereco():
    """select case"""

    user_repo = EnderecoRepository()
    endereco_select = RegisterEndereco(user_repo)

    response = None

    try:
        response = endereco_select.select_endereco(id_cliente=1)
        return response
    except:
        return {"Success": False, "Data": response}


def test_select_all_endereco():
    """case select all"""

    user_repo = EnderecoRepository()
    endereco_selectall = RegisterEndereco(user_repo)

    response = None

    try:
        response = endereco_selectall.select_all_endereco()
        return response
    except:
        return {"Success": False, "Data": response}


def test_endereco_delete():
    """case delete"""

    user_repo = EnderecoRepository()
    endereco_delete = RegisterEndereco(user_repo)

    response = None

    try:
        response = endereco_delete.delete_endereco(id_cliente=9)
        return response
    except:
        return {"Success": False, "Data": response}


def test_update_endereco():
    """case update"""

    user_repo = EnderecoRepository()
    endereco_update = RegisterEndereco(user_repo)

    response = None

    try:
        response = endereco_update.update_endereco(
            id_endereco=2,
            cep_cliente=faker.name(),
            estado=faker.name(),
            cidade=faker.name(),
            bairro=faker.name(),
            logradouro=faker.name(),
            complemento=faker.name(),
            id_cliente=6,
        )
        return response
    except:
        return {"Success": False, "Data": response}
