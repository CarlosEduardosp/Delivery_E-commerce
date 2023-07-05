from src.main.composer.register_cliente_composite import register_cliente_composer
from .adapter_cliente import AdapterCliente
from faker import Faker

faker = Faker()


def test_select_all():
    buscar = AdapterCliente(api_route=register_cliente_composer(), data={})
    response = buscar.select_all()
    print(response)


def test_select():
    buscar = AdapterCliente(
        api_route=register_cliente_composer(), data={"id_cliente": 10}
    )
    response = buscar.select()
    print(response)


def test_insert():
    buscar = AdapterCliente(
        api_route=register_cliente_composer(),
        data={
            "apelido": faker.name(),
            "email": faker.email(),
            "senha": faker.name(),
            "cep_cliente": faker.name(),
        },
    )
    response = buscar.insert()
    print(response)


def test_delete():
    buscar = AdapterCliente(
        api_route=register_cliente_composer(),
        data={"id_cliente": faker.random_number(digits=1)},
    )
    response = buscar.delete()
    print(response)


def test_update():
    buscar = AdapterCliente(
        api_route=register_cliente_composer(),
        data={
            "id_cliente": 2,
            "apelido": faker.name(),
            "email": faker.email(),
            "senha": faker.name(),
            "cep_cliente": faker.name(),
        },
    )
    response = buscar.update()
    print(response)
