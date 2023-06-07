from faker import Faker
from src.doman.models.produto import Produto

faker = Faker()


def mock_products() -> Produto:
    """Mocking products"""

    return Produto(
        nome=faker.name(),
        descricao=faker.name(),
        imagem=faker.name(),
        preco=faker.random_number(digits=2),
    )
