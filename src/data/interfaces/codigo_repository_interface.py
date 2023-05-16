from abc import ABC, abstractmethod
from typing import List
from src.doman.models.codigo import Codigo


class CodigoRepositoryInterface(ABC):

    """Interface to Pet Repository"""

    @abstractmethod
    def insert_codigo(self, codigo: int = None, id_cliente: int = None) -> Codigo:
        """Abstractmethod"""

        raise Exception("Method not implementend")

    @abstractmethod
    def select_codigo(self, id_cliente: int = None) -> List[Codigo]:
        """Abstractmethod"""

        raise Exception("Method not implementend")

    @abstractmethod
    def delete_codigo(self, id_cliente: int = None) -> None:
        """Abstractmethod"""

        raise Exception("Method not implementend")
