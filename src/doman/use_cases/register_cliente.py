from abc import ABC, abstractmethod
from src.doman.models import Cliente
from typing import Dict


class RegisterCliente(ABC):
    """Interface to RegisterUser Use case"""

    @abstractmethod
    def register(
        self, apelido: str, email: str, senha: str, cep_cliente: int
    ) -> Dict[bool, Cliente]:
        """Case"""

        raise Exception("Should implement method: register")

    @abstractmethod
    def select_cliente(
        self, id_cliente: int = None, apelido: str = None
    ) -> Dict[bool, Cliente]:
        """Case"""

        raise Exception("Should implement method: register")

    @abstractmethod
    def delete_cliente(self, id_cliente: int) -> Dict[bool, Cliente]:
        """del case"""

        raise Exception("Should implement method: register")

    @abstractmethod
    def select_all_cliente(self) -> Dict[bool, Cliente]:
        """case select all cliente"""

        raise Exception("Should implement method: register")

    @abstractmethod
    def update_cliente(
        self, id_cliente: int, apelido: str, email: str, senha: str, cep_cliente: str
    ):
        raise Exception("Should implement method: register")
