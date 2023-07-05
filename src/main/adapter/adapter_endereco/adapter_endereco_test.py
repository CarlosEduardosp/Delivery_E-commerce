from src.main.composer.register_endereco_composer import register_endereco_composer
from .adapter_endereco import AdapterEndereco
from faker import Faker

faker = Faker()


def test_select_all():
    buscar = AdapterEndereco(api_route=register_endereco_composer(), data={})
    response = buscar.select_all()
    print(response)


def select():
    buscar = AdapterEndereco(
        api_route=register_endereco_composer(), data={"id_cliente": 39}
    )
    response = buscar.select()
    print(response)


def test_insert():
    buscar = AdapterEndereco(
        api_route=register_endereco_composer(),
        data={
            "cep_cliente": faker.name(),
            "estado": faker.email(),
            "cidade": faker.name(),
            "bairro": faker.name(),
            "logradouro": faker.name(),
            "complemento": faker.name(),
            "id_cliente": 1,
        },
    )
    response = buscar.insert()
    print(response)


def test_delete():
    buscar = AdapterEndereco(
        api_route=register_endereco_composer(),
        data={"id_cliente": faker.random_number(digits=1)},
    )
    response = buscar.delete()
    print(response)


def test_update():
    buscar = AdapterEndereco(
        api_route=register_endereco_composer(),
        data={
            "id_endereco": 6,
            "cep_cliente": faker.name(),
            "estado": faker.email(),
            "cidade": faker.name(),
            "bairro": faker.name(),
            "logradouro": faker.name(),
            "complemento": faker.name(),
            "id_cliente": 39,
        },
    )
    response = buscar.update()
    print(response)
