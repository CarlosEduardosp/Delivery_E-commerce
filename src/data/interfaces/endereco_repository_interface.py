from abc import ABC, abstractmethod
from typing import List
from src.doman.models.endereco import Endereco


class EnderecoRepositoryInterface(ABC):

    """Interface to Pet Repository"""

    @abstractmethod
    def insert_endereco(
        self,
        cep_cliente: str = None,
        estado: str = None,
        cidade: str = None,
        bairro: str = None,
        logradouro: str = None,
        complemento: str = None,
        id_cliente: int = None,
    ) -> Endereco:
        """Abstractmethod"""

        raise Exception("Method not implementend")

    @abstractmethod
    def select_endereco(self, id_cliente: int = None) -> List[Endereco]:
        """Abstractmethod"""

        raise Exception("Method not implementend")

    @abstractmethod
    def delete_endereco(self, id_cliente: int = None) -> None:
        """Abstractmethod"""

        raise Exception("Method not implementend")
