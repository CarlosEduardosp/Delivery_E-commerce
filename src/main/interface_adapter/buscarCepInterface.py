from typing import Type, Dict
from abc import ABC, abstractmethod
from src.main.interface.route_buscar_cep import RouteInterface as Route


class BuscarCepInterface(ABC):
    """Interface to Routes"""

    @abstractmethod
    def adapter_buscar_cep(self, api_route: Type[Route], data: Type[Dict]) -> any:
        """Adapter pattern to Flask
        :param - api_route - RouteInterface
        :param - data - dicionario com os dados da requisição
        :param - action - ação com as opções de string ('cep_cliente')
        :api_route: Composite Routes
        """

        raise Exception("Should implement method: route")
