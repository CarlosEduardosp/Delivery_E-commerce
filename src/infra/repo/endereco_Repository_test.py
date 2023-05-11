# pylint: disable=E1101
from .endereco_Repository import EnderecoRepository
from faker import Faker

endereco_repository = EnderecoRepository()
faker = Faker()


def test_insert_endereco():
    """should insert User"""

    cep_cliente = faker.random_number(digits=8)
    estado = faker.name()
    cidade = faker.name()
    bairro = faker.name()
    logradouro = faker.name()
    complemento = faker.name()
    id_cliente = faker.random_number(digits=1)

    try:
        new_end = endereco_repository.insert_endereco(
            cep_cliente=cep_cliente,
            estado=estado,
            cidade=cidade,
            bairro=bairro,
            logradouro=logradouro,
            complemento=complemento,
            id_cliente=id_cliente,
        )

        print("Inserção de endereço finalizada com Sucesso.", new_end.cep_cliente)

    except:
        print("OCORREU UM ERRO ao inserir endereço.")


def test_select_endereco():
    """Select in users"""

    try:
        data = endereco_repository.select_endereco(id_cliente=5)
        for i in data:
            print("Select Ok -", i.estado)
    except:
        print("Usuario não encontrado.")


def delete_endereco():
    try:
        endereco_repository.delete_endereco(id_cliente=2)
        print("Endereco Deletado com Sucesso.")
    except:
        print("Cliente Não Encontrado.")
