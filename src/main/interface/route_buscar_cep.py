from typing import Type
from abc import ABC, abstractmethod
from src.presenters.helpers.http_models import HttpRequest, HttpResponse


class RouteInterface(ABC):
    """Interface to Routes"""

    @abstractmethod
    def route_buscar_cep(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Defining Route"""

        raise Exception("Should implement method: route")
