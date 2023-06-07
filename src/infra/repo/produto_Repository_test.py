# pylint: disable=E1101
from .produto_Repository import ProdutoRepository
from faker import Faker

produto_repository = ProdutoRepository()
faker = Faker()


def test_insert_produto():
    """should insert User"""

    nome = faker.random_number(digits=1)
    descricao = faker.name()
    imagem = faker.name()
    preco = faker.random_number(digits=2)

    try:
        # SQL comands
        new_produto = produto_repository.insert_produto(
            nome=nome, descricao=descricao, imagem=imagem, preco=preco
        )

        print("Inserção finalizada com Sucesso.", new_produto.id_produto)

    except:
        print("ERRO - Produto já existe")


def test_select_produto():
    """Select in users"""

    try:
        data = produto_repository.select_produto(id_produto=1)
        for i in data:
            print("Select Ok -", i.id_produto)
    except:
        print("Produto não encontrado.")


def test_delete_produto():
    try:
        produto_repository.delete_produto(id_produto=10)
        print("Produto Deletado com Sucesso.")
    except:
        print("Produto Não Encontrado.")


def test_update_produto():
    """deleting data in cliente"""

    try:
        id_produto = 2
        nome = faker.random_number(digits=1)
        descricao = faker.name()
        imagem = faker.name()
        preco = faker.random_number(digits=2)

        produto_repository.update_produto(
            id_produto=id_produto,
            nome=nome,
            descricao=descricao,
            imagem=imagem,
            preco=preco,
        )
        print(f"Alteração realizada com Sucesso.")

    except:
        print("Produto não encontrado.")
