from .buscar_cep import BuscarCep


def buscar_cep():
    endereco = BuscarCep()
    endereco.pesquisar_cep("26515570")
    print(endereco)
