from typing import Type
from abc import ABC, abstractmethod
from src.presenters.helpers.http_models import HttpRequest, HttpResponse


class RouteInterface(ABC):
    """Interface to Routes"""

    @abstractmethod
    def route_insert(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Defining Route"""

        raise Exception("Should implement method: route")

    @abstractmethod
    def route_select(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Defining Route"""

        raise Exception("Should implement method: route")

    @abstractmethod
    def route_delete(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Defining Route"""

        raise Exception("Should implement method: route")

    @abstractmethod
    def route_select_all(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Defining Route"""

        raise Exception("Should implement method: route")

    @abstractmethod
    def route_update(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Defining Route"""

        raise Exception("Should implement method: route")
