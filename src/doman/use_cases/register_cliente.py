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
    def select_cliente(self, id_cliente: int) -> Dict[bool, Cliente]:
        """Case"""

        raise Exception("Should implement method: register")
