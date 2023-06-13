from abc import ABC, abstractmethod
from src.doman.models import Carrinho
from typing import Dict


class RegisterCarrinho(ABC):
    """Interface to Registercarrinho Use case"""

    @abstractmethod
    def insert_carrinho(self, id_produto: int, id_cliente: int) -> Dict[bool, Carrinho]:
        """Case"""

        raise Exception("Should implement method: register")

    @abstractmethod
    def select_carrinho(self, id_cliente: int) -> Dict[bool, Carrinho]:
        """Case"""

        raise Exception("Should implement method: register")

    @abstractmethod
    def delete_carrinho(self, id_cliente: int, id_produto: int) -> Dict[bool, Carrinho]:
        """del case"""

        raise Exception("Should implement method: register")

    @abstractmethod
    def select_all_carrinho(self) -> Dict[bool, Carrinho]:
        """case select all cliente"""

        raise Exception("Should implement method: register")
