# pylint: disable=E1101
from .imagemperfil_Repository import ImagemPerfilRepository
from faker import Faker

imagem_repository = ImagemPerfilRepository
faker = Faker()


def test_insert_imagem():
    """should insert imagem"""

    imagem = faker.name()

    try:
        # SQL comands
        new_imagem = imagem_repository.insert_imagem(imagem=imagem)

        assert new_imagem.imagem == imagem

        print("Inserção finalizada com Sucesso.", new_imagem.imagem)

    except:
        print("ERRO ao inserir dados")


def test_select_imagem():
    """Select in codigo"""

    try:
        data = imagem_repository.select_imagem()
        for i in data:
            print("Select Imagem Ok -", i.imagem)
    except:
        print("Imagem não encontrado.")


def test_delete_imagem():
    try:
        imagem_repository.delete_imagem()
        print("Imagem Deletado com Sucesso.")
    except:
        print("Imagem Não Encontrado.")
