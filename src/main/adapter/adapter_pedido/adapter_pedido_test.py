from src.main.composer.register_pedido_composer import register_pedido_composer
from .adapter_pedido import AdapterPedido
from faker import Faker

faker = Faker()


def test_select_all():
    buscar = AdapterPedido(api_route=register_pedido_composer(), data={})
    response = buscar.select_all()
    print(response)


def test_select():
    buscar = AdapterPedido(
        api_route=register_pedido_composer(), data={"id_cliente": 8, "id_pedido": 1}
    )
    response = buscar.select()
    print(response)


def test_insert():
    buscar = AdapterPedido(
        api_route=register_pedido_composer(),
        data={
            "id_cliente": faker.random_number(digits=1),
            "id_produto": faker.random_number(digits=1),
            "numero_pedido": faker.random_number(digits=1),
            "valor": float(faker.random_number(digits=1)),
            "data_pedido": faker.name(),
            "status": faker.name(),
        },
    )
    response = buscar.insert()
    print(response)


def test_delete():
    buscar = AdapterPedido(
        api_route=register_pedido_composer(),
        data={
            "id_cliente": faker.random_number(digits=1),
            "id_pedido": faker.random_number(digits=1),
        },
    )
    response = buscar.delete()
    print(response)


def test_update():
    buscar = AdapterPedido(
        api_route=register_pedido_composer(),
        data={
            "id_pedido": 1,
            "id_cliente": faker.random_number(digits=1),
            "id_produto": faker.random_number(digits=1),
            "numero_pedido": faker.random_number(digits=1),
            "valor": float(faker.random_number(digits=1)),
            "data_pedido": faker.name(),
            "status": faker.name(),
        },
    )
    response = buscar.update()
    print(response)
