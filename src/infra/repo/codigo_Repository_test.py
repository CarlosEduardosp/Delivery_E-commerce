# pylint: disable=E1101
from .codigo_Repository import CodigoRepository
from faker import Faker

codigo_repository = CodigoRepository
faker = Faker()


def test_insert_codigo():
    """should insert Codigo"""

    codigo = faker.random_number(digits=3)

    try:
        # SQL comands
        new_codigo = codigo_repository.insert_codigo(codigo=codigo)

        assert new_codigo.codigo == codigo

        print("Inserção finalizada com Sucesso.", new_codigo.codigo)

    except:
        print("ERRO ao inserir dados")


def test_select_codigo():
    """Select in codigo"""

    try:
        data = codigo_repository.select_codigo()
        for i in data:
            print("Select Codigo Ok -", i.codigo)
    except:
        print("Codigo não encontrado.")


def test_delete_codigo():
    try:
        codigo_repository.delete_codigo()
        print("Codigo Deletado com Sucesso.")
    except:
        print("Codigo Não Encontrado.")
