from src.main.composer.register_codigo_composer import register_codigo_composer
from .adapter_codigo import AdapterCodigo
from faker import Faker

faker = Faker()


def test_select():
    buscar = AdapterCodigo(api_route=register_codigo_composer(), data={"id_cliente": 2})
    response = buscar.select()
    print(response)


def test_insert():
    buscar = AdapterCodigo(
        api_route=register_codigo_composer(),
        data={
            "id_cliente": faker.random_number(digits=1),
            "codigo": faker.random_number(digits=4),
        },
    )
    response = buscar.insert()
    print(response)


def test_delete():
    buscar = AdapterCodigo(
        api_route=register_codigo_composer(),
        data={"id_cliente": faker.random_number(digits=2)},
    )
    response = buscar.delete()
    print(response)
