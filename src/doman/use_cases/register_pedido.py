from abc import ABC, abstractmethod
from src.doman.models import Pedido
from typing import Dict


class RegisterPedido(ABC):
    """Interface to RegisterPedido Use case"""

    @abstractmethod
    def insert_pedido(
        self,
        id_cliente: int,
        id_produto: int,
        numero_pedido: int,
        valor: float,
        data_pedido: str,
        status: str,
    ) -> Dict[bool, Pedido]:
        """Case"""

        raise Exception("Should implement method: insert_pedido")

    @abstractmethod
    def select_all_pedido(self) -> Dict[bool, Pedido]:
        """case select all pedido"""

        raise Exception("Should implement method: select_all")

    @abstractmethod
    def select_pedido(self, id_cliente: int, id_pedido: int) -> Dict[bool, Pedido]:
        """Case"""

        raise Exception("Should implement method: select")

    @abstractmethod
    def delete_pedido(self, id_pedido: int, id_cliente: int) -> Dict[bool, Pedido]:
        """delete in case"""

        raise Exception("Should implement method: delete")

    @abstractmethod
    def update_pedido(
        self,
        id_pedido: int,
        id_cliente: int,
        id_produto: int,
        numero_pedido: int,
        valor: float,
        data_pedido: str,
        status: str,
    ) -> Dict[bool, Pedido]:
        raise Exception("Should implement method: update")
