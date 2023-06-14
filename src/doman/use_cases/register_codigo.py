from abc import ABC, abstractmethod
from src.doman.models import Codigo
from typing import Dict


class RegisterCodigo(ABC):
    """Interface to Registercodigo Use case"""

    @abstractmethod
    def insert_codigo(self, codigo: int, id_cliente: int) -> Dict[bool, Codigo]:
        """Case"""

        raise Exception("Should implement method: register")

    @abstractmethod
    def select_codigo(self, id_cliente: int) -> Dict[bool, Codigo]:
        """Case"""

        raise Exception("Should implement method: register")

    @abstractmethod
    def delete_codigo(self, id_cliente: int) -> Dict[bool, Codigo]:
        """del case"""

        raise Exception("Should implement method: register")
