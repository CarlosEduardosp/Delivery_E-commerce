from abc import ABC, abstractmethod
from typing import List
from src.doman.models.carrinho import Carrinho


class CarrinhoRepositoryInterface(ABC):

    """Interface to Pet Repository"""

    @abstractmethod
    def insert_carrinho(
        self, id_produto: int = None, id_cliente: int = None
    ) -> Carrinho:
        """Abstractmethod"""

        raise Exception("Method not implementend")

    @abstractmethod
    def select_carrinho(self, id_cliente: int = None) -> List[Carrinho]:
        """Abstractmethod"""

        raise Exception("Method not implementend")

    @abstractmethod
    def delete_carrinho(self, id_cliente: int = None, id_produto: int = None) -> None:
        """Abstractmethod"""

        raise Exception("Method not implementend")

    @abstractmethod
    def select_all_carrinho(self) -> List[Carrinho]:
        """case select all"""

        raise Exception("Method not implementend")
