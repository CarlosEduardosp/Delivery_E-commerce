from abc import ABC, abstractmethod
from src.doman.models import Endereco
from typing import Dict


class RegisterEndereco(ABC):
    """Interface to RegisterUser Use case"""

    @abstractmethod
    def insert_endereco(
        self,
        cep_cliente: str,
        estado: str,
        cidade: str,
        bairro: str,
        logradouro: str,
        complemento: str,
        id_cliente: int,
    ) -> Dict[bool, Endereco]:
        """Case"""

        raise Exception("Should implement method: register")

    @abstractmethod
    def select_endereco(self, id_cliente: int) -> Dict[bool, Endereco]:
        """Case"""

        raise Exception("Should implement method: register")

    @abstractmethod
    def delete_endereco(self, id_cliente: int) -> Dict[bool, Endereco]:
        """del case"""

        raise Exception("Should implement method: register")

    @abstractmethod
    def select_all_endereco(self) -> Dict[bool, Endereco]:
        """case select all endereco"""

        raise Exception("Should implement method: register")

    @abstractmethod
    def update_endereco(
        self,
        id_endereco: int,
        cep_cliente: str,
        estado: str,
        cidade: str,
        bairro: str,
        logradouro: str,
        complemento: str,
        id_cliente: int,
    ):
        raise Exception("Should implement method: register")
