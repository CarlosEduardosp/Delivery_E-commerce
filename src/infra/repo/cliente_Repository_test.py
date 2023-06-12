# pylint: disable=E1101
from .cliente_Repository import ClienteRepository
from faker import Faker

cliente_repository = ClienteRepository()
faker = Faker()


def test_insert_cliente():
    """should insert User"""

    apelido = faker.name()
    senha = faker.password()
    email = faker.email()
    cep_cliente = faker.random_number(digits=8)

    try:
        # SQL comands
        new_cliente = cliente_repository.insert_cliente(
            apelido, email, senha, cep_cliente
        )

        assert new_cliente.apelido == apelido
        assert new_cliente.email == email
        assert new_cliente.senha == senha

        print("Inserção finalizada com Sucesso!!", new_cliente)

    except:
        print("ERRO - Usuário já existe")


def test_select_cliente():
    """Select in users"""

    try:
        data = cliente_repository.select_cliente(id_cliente=2)
        for i in data:
            print("Select Ok -", i.apelido)
    except:
        print("Usuario não encontrado.")


def test_delete_cliente():
    try:
        cliente_repository.delete_cliente(id_cliente=10)
        print("Cliente Deletado com Sucesso.")
    except:
        print("Cliente Não Encontrado.")


def test_update_cliente():
    """deleting data in cliente"""

    try:
        apelido = faker.name()
        senha = faker.password()
        email = faker.email()
        cep_cliente = faker.random_number(digits=8)

        cliente_repository.update_cliente(
            id_cliente=3,
            apelido=apelido,
            senha=senha,
            email=email,
            cep_cliente=cep_cliente,
        )
        print(f"Alteração realizada com Sucesso.")

    except:
        print("Cliente não encontrado.")
