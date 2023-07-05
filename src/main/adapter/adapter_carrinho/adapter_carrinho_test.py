from src.main.composer.register_carrinho_composer import register_carrinho_composer
from .adapter_carrinho import AdapterCarrinho
from faker import Faker

faker = Faker()


def test_select_all():
    buscar = AdapterCarrinho(api_route=register_carrinho_composer(), data={})
    response = buscar.select_all()
    print(response)


def test_select():
    buscar = AdapterCarrinho(
        api_route=register_carrinho_composer(), data={"id_cliente": 8}
    )
    response = buscar.select()
    print(response)


def test_insert():
    buscar = AdapterCarrinho(
        api_route=register_carrinho_composer(),
        data={
            "id_produto": faker.random_number(digits=1),
            "id_cliente": faker.random_number(digits=1),
        },
    )
    response = buscar.insert()
    print(response)


def test_delete():
    buscar = AdapterCarrinho(
        api_route=register_carrinho_composer(),
        data={
            "id_produto": faker.random_number(digits=1),
            "id_cliente": faker.random_number(digits=1),
        },
    )
    response = buscar.delete()
    print(response)
