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


def test_select_produto():
    """testing select produto"""

    user_repo = ProdutoRepository()
    register_produto = RegisterProduto(user_repo)

    try:
        response_2 = register_produto.select_produto(
            id_produto=faker.random_number(digits=2)
        )

        if response_2["Success"]:
            for i in response_2["Data"]:
                nome = i.nome
                descricao = i.descricao
                imagem = i.imagem
                preco = i.preco
                id_produto = i.id_produto

            response = {
                "id_produto": id_produto,
                "nome": nome,
                "descricao": descricao,
                "imagem": imagem,
                "preco": preco,
            }
            return {"Success": True, "Data": response}
    except:
        return {"Success": False, "Data": None}
