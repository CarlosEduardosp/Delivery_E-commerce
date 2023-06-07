from faker import Faker
from .register_produto import RegisterProduto
from src.infra.repo.produto_Repository import ProdutoRepository

faker = Faker()


def test_register_produto():
    """testing registry method"""

    user_repo = ProdutoRepository()
    register_produto = RegisterProduto(user_repo)

    attributes = {
        "nome": faker.name(),
        "descricao": faker.name(),
        "imagem": faker.name(),
        "preco": float(faker.random_number(digits=2)),
    }

    response = register_produto.register(
        nome=attributes["nome"],
        descricao=attributes["descricao"],
        imagem=attributes["imagem"],
        preco=attributes["preco"],
    )

    # testing input

    # testing outputs
    assert response["Success"] is True
    assert response["Data"]

    return response
