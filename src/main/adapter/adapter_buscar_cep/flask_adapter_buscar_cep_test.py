from .flask_adapter_buscar_cep import BuscarCep
from src.main.composer.buscar_cep_composer import buscar_cep_composer


def test_buscar_cep():
    """testando buscar cep"""
    buscar_cep = BuscarCep(
        api_route=buscar_cep_composer(), data={"cep_cliente": "26515570"}
    )

    response = buscar_cep.adapter_buscar_cep()
    print(response)
