from faker import Faker
from src.data.buscar_cep.buscar_cep import BuscarCep
from src.presenters.helpers.http_models import HttpRequest
from .buscar_cep_controller import BuscarCepController


faker = Faker()


def test_select_cep():
    """Testing Handle method"""

    buscar_cep_controller = BuscarCepController(BuscarCep())

    http_request = HttpRequest(query={"cep_cliente": "26515570"})

    response = buscar_cep_controller.route_buscar_cep(http_request)

    return response
