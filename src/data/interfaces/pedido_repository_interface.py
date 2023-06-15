from abc import ABC, abstractmethod
from typing import List
from src.doman.models.pedido import Pedido


class PedidoRepositoryInterface(ABC):

    """Interface to Pet Repository"""

    @abstractmethod
    def insert_pedido(
        self,
        id_cliente: int = None,
        id_produto: int = None,
        numero_pedido: int = None,
        valor: float = None,
        data_pedido: str = None,
        status: str = None,
    ) -> Pedido:
        """Abstractmethod"""

        raise Exception("Method not implementend")

    @abstractmethod
    def select_pedido(
        self, id_pedido: int = None, id_cliente: int = None
    ) -> List[Pedido]:
        """Abstractmethod"""

        raise Exception("Method not implementend")

    @abstractmethod
    def delete_pedido(self, id_pedido: int = None, id_cliente: int = None) -> None:
        """Abstractmethod"""

        raise Exception("Method not implementend")

    @abstractmethod
    def update_pedido(
        self,
        id_pedido: int = None,
        id_cliente: int = None,
        id_produto: int = None,
        numero_pedido: int = None,
        valor: float = None,
        data_pedido: str = None,
        status: str = None,
    ) -> List[Pedido]:
        """Abstractmethod"""

        raise Exception("Method not implementend")

    @abstractmethod
    def select_all_pedido(self) -> List[Pedido]:
        """Abstractmethod"""

        raise Exception("Method not implementend")
