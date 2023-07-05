from src.main.composer.register_produto_composer import register_produto_composer
from .adapter_produto import AdapterProduto
from faker import Faker

faker = Faker()


def test_select_all():
    buscar = AdapterProduto(api_route=register_produto_composer(), data={})
    response = buscar.select_all()
    print(response)


def select():
    buscar = AdapterProduto(
        api_route=register_produto_composer(), data={"id_produto": 9}
    )
    response = buscar.select()
    print(response)


def test_insert():
    buscar = AdapterProduto(
        api_route=register_produto_composer(),
        data={
            "nome": faker.name(),
            "descricao": faker.email(),
            "imagem": faker.name(),
            "preco": float(faker.random_number(digits=2)),
        },
    )
    response = buscar.insert()
    print(response)


def test_delete():
    buscar = AdapterProduto(
        api_route=register_produto_composer(),
        data={"id_produto": faker.random_number(digits=1)},
    )
    response = buscar.delete()
    print(response)


def test_update():
    buscar = AdapterProduto(
        api_route=register_produto_composer(),
        data={
            "id_produto": faker.random_number(digits=9),
            "nome": faker.name(),
            "descricao": faker.email(),
            "imagem": faker.name(),
            "preco": float(faker.random_number(digits=2)),
        },
    )
    response = buscar.update()
    print(response)
