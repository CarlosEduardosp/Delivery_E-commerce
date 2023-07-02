# pylint: disable=E1101
from .pedido_Repository import PedidoRepository
from faker import Faker

pedido_repository = PedidoRepository()
faker = Faker()

id_cliente = faker.random_number(digits=1)


def test_insert_pedido():
    """should insert User"""

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


def test_select_pedido():
    """Select in users"""

    try:
        data = pedido_repository.select_pedido(id_pedido=201, id_cliente=1)
        print("Select Ok -", data)
    except:
        print("Pedido não encontrado.")


def test_select_all_pedido():
    """select all pedido test"""

    try:
        response = pedido_repository.select_all_pedido()
        print("tudo Ok", response)
    except:
        print("Algo deu errado!!")


def test_delete_pedido():
    try:
        pedido_repository.delete_pedido(id_pedido=4, id_cliente=8)
        print("Pedido Deletado com Sucesso.")
    except:
        print("Pedido Não Encontrado.")


def test_update_cliente():
    """deleting data in cliente"""

    try:
        id_cliente = faker.random_number(digits=1)
        id_produto = faker.random_number(digits=1)
        numero_pedido = faker.random_number(digits=1)
        valor = faker.random_number(digits=2)
        data_pedido = faker.name()
        status = faker.name()
        id_pedido = 3

        data = pedido_repository.update_pedido(
            id_pedido=id_pedido,
            id_cliente=id_cliente,
            id_produto=id_produto,
            numero_pedido=numero_pedido,
            valor=valor,
            data_pedido=data_pedido,
            status=status,
        )
        print(f"Alteração realizada com Sucesso.", data)

    except:
        print("Pedido não encontrado.")
