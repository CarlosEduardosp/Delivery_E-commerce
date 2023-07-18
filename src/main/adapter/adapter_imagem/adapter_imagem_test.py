from src.main.composer.register_imagem_composer import register_imagem_composer
from .adapter_imagem import AdapterImagem
from faker import Faker

faker = Faker()


def test_select():
    buscar = AdapterImagem(api_route=register_imagem_composer(), data={})
    response = buscar.select()
    print(response)


def insert():
    buscar = AdapterImagem(
        api_route=register_imagem_composer(), data={"imagem": faker.name()}
    )
    response = buscar.insert()
    print(response)


def delete():
    buscar = AdapterImagem(api_route=register_imagem_composer(), data={})
    response = buscar.delete()
    print(response)
