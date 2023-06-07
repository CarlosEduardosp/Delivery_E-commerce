from faker import Faker
from src.doman.models.cliente import Cliente

faker = Faker()


def mock_users() -> Cliente:
    """Mocking Users"""

    return Cliente(
        id_cliente=faker.random_number(digits=1),
        apelido=faker.name(),
        email=faker.name(),
        senha=faker.name(),
        cep_cliente=faker.random_number(digits=5),
    )
