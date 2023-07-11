from faker import Faker
from .registrar_pedido import RegisterPedido
from src.infra.repo.pedido_Repository import PedidoRepository

faker = Faker()


def insert_pedido():
    """testing insert pedido"""

    user_repo = PedidoRepository()
    registerPedido = RegisterPedido(user_repo)

    response = registerPedido.insert_pedido(
        id_cliente=faker.random_number(digits=1),
        id_produto=faker.random_number(digits=1),
        numero_pedido=faker.random_number(digits=1),
        valor=float(faker.random_number(digits=1)),
        data_pedido=faker.name(),
        status=faker.name(),
    )
    return response


def test_select_pedido():
    """testing select pedido"""

    user_repo = PedidoRepository()
    registerPedido = RegisterPedido(user_repo)

    response = registerPedido.select_pedido(id_cliente=1)
    for i in response["Data"]:
        print(i.valor)

    return response


def select_all():
    """testing selct all pedido"""

    user_repo = PedidoRepository()
    registerPedido = RegisterPedido(user_repo)

    response = registerPedido.select_all_pedido()

    return response


def delete_pedido():
    """testing use case delete pedido"""

    user_repo = PedidoRepository()
    registerPedido = RegisterPedido(user_repo)

    response = registerPedido.delete_pedido(id_pedido=5, id_cliente=4)

    return response


def update_pedido():
    """testing update use case in pedido"""

    user_repo = PedidoRepository()
    registerPedido = RegisterPedido(user_repo)

    response = registerPedido.update_pedido(
        id_pedido=1,
        id_cliente=faker.random_number(digits=1),
        id_produto=faker.random_number(digits=1),
        numero_pedido=faker.random_number(digits=2),
        valor=float(faker.random_number(digits=2)),
        data_pedido=faker.name(),
        status=faker.name(),
    )
    return response
