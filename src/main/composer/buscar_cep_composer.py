from src.main.interface.route_buscar_cep import RouteInterface
from src.presenters.controllers.buscar_cep_controller import BuscarCepController
from src.data.buscar_cep.buscar_cep import BuscarCep


def buscar_cep_composer() -> RouteInterface:
    """Composing buscar cep Route
    :param - None
    :return - Object with Register User Route
    """

    use_case = BuscarCep()
    buscar_cep_route = BuscarCepController(use_case)

    return buscar_cep_route
