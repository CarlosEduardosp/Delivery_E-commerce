from abc import ABC, abstractmethod
from typing import List
from src.doman.models.cliente import Cliente


class ClienteRepositoryInterface(ABC):

    """Interface to Pet Repository"""

    @abstractmethod
    def insert_cliente(self, name: str, password: str) -> Cliente:
        """Abstractmethod"""

        raise Exception("Method not implementend")

    @abstractmethod
    def select_cliente(self, id_cliente: int = None) -> List[Cliente]:
        """Abstractmethod"""

        raise Exception("Method not implementend")

    @abstractmethod
    def delete_cliente(self, id_cliente: int = None) -> List[Cliente]:
        """Abstractmethod"""

        raise Exception("Method not implementend")
