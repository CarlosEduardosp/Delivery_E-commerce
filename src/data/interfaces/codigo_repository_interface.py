from abc import ABC, abstractmethod
from typing import List
from src.doman.models.codigo import Codigo


class CodigoRepositoryInterface(ABC):

    """Interface to Pet Repository"""

    @abstractmethod
    def insert_codigo(self, codigo: int = None) -> Codigo:
        """Abstractmethod"""

        raise Exception("Method not implementend")

    @abstractmethod
    def select_codigo(self) -> List[Codigo]:
        """Abstractmethod"""

        raise Exception("Method not implementend")

    @abstractmethod
    def delete_codigo(self) -> None:
        """Abstractmethod"""

        raise Exception("Method not implementend")
