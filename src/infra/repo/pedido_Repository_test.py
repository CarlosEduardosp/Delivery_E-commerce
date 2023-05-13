# pylint: disable=E1101
from .pedido_Repository import PedidoRepository
from faker import Faker

pedido_repository = PedidoRepository()
faker = Faker()


def test_insert_pedido():
    """should insert User"""

    id_cliente = faker.random_number(digits=1)
    id_produto = faker.random_number(digits=1)
    numero_pedido = faker.random_number(digits=1)
    valor = faker.random_number(digits=2)
    data_pedido = faker.name()
    status = faker.name()

    try:
        # SQL comands
        new_pedido = pedido_repository.insert_pedido(
            id_cliente=id_cliente,
            id_produto=id_produto,
            numero_pedido=numero_pedido,
            valor=valor,
            data_pedido=data_pedido,
            status=status,
        )

        print("Inserção finalizada com Sucesso.", new_pedido.id_cliente)

    except:
        print("ERRO - pedido já existe")
