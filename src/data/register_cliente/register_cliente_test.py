from faker import Faker
from .register_cliente import RegisterCliente
from src.infra.repo.cliente_Repository import ClienteRepository

faker = Faker()


def test_register():
    """testing registry method"""

    user_repo = ClienteRepository()
    register_user = RegisterCliente(user_repo)

    attributes = {
        "apelido": faker.name(),
        "email": faker.email(),
        "senha": faker.name(),
        "cep_cliente": faker.name(),
    }

    response = register_user.register(
        apelido=attributes["apelido"],
        email=attributes["email"],
        senha=attributes["senha"],
        cep_cliente=attributes["cep_cliente"],
    )

    # testing input
    # assert user_repo.insert_user_params["apelido"] == attributes["apelido"]
    # assert user_repo.insert_user_params["email"] == attributes["email"]
    # assert user_repo.insert_user_params["senha"] == attributes["senha"]
    # assert user_repo.insert_user_params["cep_cliente"] == attributes["cep_cliente"]

    # testing outputs
    # assert response["Success"] is True
    # assert response["Data"]

    return response


def test_select_cliente():
    """selecting cliente"""

    user_repo = ClienteRepository()
    select_cliente = RegisterCliente(user_repo)

    try:
        response = select_cliente.select_cliente(id_cliente=2)

        if response["Success"]:
            for i in response["Data"]:
                apelido = i.apelido
                email = i.email
                senha = i.senha
                cep_cliente = i.cep_cliente
                id_cliente = i.id_cliente

            response = {
                "id_cliente": id_cliente,
                "apelido": apelido,
                "email": email,
                "senha": senha,
                "cep_cliente": cep_cliente,
            }
            return {"Success": True, "Data": response}

        return response
    except:
        return {"Success": False, "Data": None}


def test_delete_cliente():
    """del cliente"""

    user_repo = ClienteRepository()
    register_user = RegisterCliente(user_repo)

    try:
        response = register_user.delete_cliente(
            id_cliente=faker.random_number(digits=1)
        )
    except:
        response = {"Success": False, "Data": None}

    return response


def test_select_all():
    """select all clientes"""

    user_repo = ClienteRepository()
    register_user = RegisterCliente(user_repo)

    response = register_user.select_all_cliente()

    return response


def test_update_cliente():
    """update cliente"""

    user_repo = ClienteRepository()
    register_user = RegisterCliente(user_repo)

    response = register_user.update_cliente(
        id_cliente=4,
        apelido=faker.name(),
        email=faker.email(),
        senha=faker.name(),
        cep_cliente=faker.name(),
    )
    return response
