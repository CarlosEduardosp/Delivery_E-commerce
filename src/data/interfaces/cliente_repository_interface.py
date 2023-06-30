from abc import ABC, abstractmethod
from typing import List
from src.doman.models.cliente import Cliente


class ClienteRepositoryInterface(ABC):

    """Interface to Cliente Repository"""

    @abstractmethod
    def insert_cliente(
        self, apelido: str, email: str, senha: str, cep_cliente: int
    ) -> Cliente:
        """Abstractmethod"""

        raise Exception("Method not implementend")

    @abstractmethod
    def select_cliente(
        self, id_cliente: int = None, apelido: str = None
    ) -> List[Cliente]:
        """Abstractmethod"""

        raise Exception("Method not implementend")

    @abstractmethod
    def delete_cliente(self, id_cliente: int = None) -> List[Cliente]:
        """Abstractmethod"""

        raise Exception("Method not implementend")

    @abstractmethod
    def select_all_cliente(self) -> List[Cliente]:
        """Abstractmethod"""

        raise Exception("Method not implementend")

    @abstractmethod
    def update_cliente(
        self,
        id_cliente: int = None,
        apelido: str = None,
        email: str = None,
        senha: str = None,
        cep_cliente: str = None,
    ) -> List[Cliente]:
        """Abstractmethod"""

        raise Exception("Method not implementend")
