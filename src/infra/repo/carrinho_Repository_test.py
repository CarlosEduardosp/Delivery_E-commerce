# pylint: disable=E1101
from .carrinho_Repository import CarrinhoRepository
from faker import Faker

carrinho_repository = CarrinhoRepository()
faker = Faker()


def test_insert_carrinho():
    """should insert Carrinho"""

    id_produto = faker.random_number(digits=1)
    id_cliente = faker.random_number(digits=1)

    try:
        # SQL comands
        new_carrinho = carrinho_repository.insert_carrinho(
            id_produto=id_produto, id_cliente=id_cliente
        )

        assert new_carrinho.id_produto == id_produto
        assert new_carrinho.id_cliente == id_cliente

        print("Inserção finalizada com Sucesso.", new_carrinho.id_produto)

    except:
        print("ERRO ao inserir dados")


def test_select_carrinho():
    """Select in carrinho"""

    try:
        data = carrinho_repository.select_carrinho(id_cliente=2)
        for i in data:
            print("Select Carrinho Ok -", i.id_produto)
    except:
        print("Carrinho não encontrado.")


def test_delete_carrinho():
    try:
        carrinho_repository.delete_carrinho(id_cliente=7, id_produto=0)
        print("Carrinho Deletado com Sucesso.")
    except:
        print("Carrinho Não Encontrado.")
