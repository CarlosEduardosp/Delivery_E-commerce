from faker import Faker
from .register_cliente import RegisterCliente
from src.infra.test.user_repository_spy import UserRepositorySpy

faker = Faker()


def test_register():
    """testing registry method"""

    user_repo = UserRepositorySpy()
    register_user = RegisterCliente(user_repo)

    attributes = {
        "apelido": faker.name(),
        "email": faker.name(),
        "senha": faker.name(),
        "cep_cliente": faker.random_number(digits=8),
    }

    response = register_user.register(
        apelido=attributes["apelido"],
        email=attributes["email"],
        senha=attributes["senha"],
        cep_cliente=attributes["cep_cliente"],
    )

    # testing input
    assert user_repo.insert_user_params["apelido"] == attributes["apelido"]
    assert user_repo.insert_user_params["email"] == attributes["email"]
    assert user_repo.insert_user_params["senha"] == attributes["senha"]
    assert user_repo.insert_user_params["cep_cliente"] == attributes["cep_cliente"]

    # testing outputs
    # assert response["Success"] is True
    # assert response["Data"]

    return response
