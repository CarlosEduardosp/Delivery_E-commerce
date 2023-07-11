from typing import Type, Dict
from src.doman.use_cases.register_pedido import (
    RegisterPedido as RegisterPedidoInterface,
)
from src.data.interfaces.pedido_repository_interface import (
    PedidoRepositoryInterface as PedidoRepository,
)
from src.doman.models.pedido import Pedido


class RegisterPedido(RegisterPedidoInterface):
    """Class to define usercase: Register imagem"""

    def __init__(self, pedido_repository: Type[PedidoRepository]):
        self.pedido_repository = pedido_repository

    def insert_pedido(
        self,
        id_cliente: int,
        id_produto: int,
        numero_pedido: int,
        valor: float,
        data_pedido: str,
        status: str,
    ) -> Dict[bool, Pedido]:
        """case insert pedido"""

        response = None
        validate_entry = (
            isinstance(id_cliente, int)
            and isinstance(id_produto, int)
            and isinstance(numero_pedido, int)
            and isinstance(valor, float)
            and isinstance(data_pedido, str)
            and isinstance(status, str)
        )

        if validate_entry:
            response = self.pedido_repository.insert_pedido(
                id_cliente=id_cliente,
                id_produto=id_produto,
                numero_pedido=numero_pedido,
                valor=valor,
                data_pedido=data_pedido,
                status=status,
            )
            return {"Success": True, "Data": response}

        return {"Success": False, "Data": response}

    def select_pedido(self, id_cliente: int) -> Dict[bool, Pedido]:
        """use case select pedido"""

        response = None
        try:
            response = self.pedido_repository.select_pedido(id_cliente=id_cliente)
            return {"Success": True, "Data": response}
        except:
            return {"Success": False, "Data": response}

    def select_all_pedido(self) -> Dict[bool, Pedido]:
        """use case select all"""

        response = None
        try:
            todos_os_ids = []
            response = self.pedido_repository.select_all_pedido()
            response_dict = []
            for i in response:
                todos_os_ids.append(i.id_pedido)
                response_dict.append(i)
            quantidade = len(todos_os_ids)

            return {"Success": True, "Data": response_dict, "Len": quantidade}
        except:
            return {"Success": False, "Data": response}

    def delete_pedido(self, id_pedido: int, id_cliente: int) -> Dict[bool, Pedido]:
        """use case delete"""

        response = None

        try:
            response = self.pedido_repository.delete_pedido(
                id_pedido=id_pedido, id_cliente=id_cliente
            )
            return {"Success": True, "Data": response}
        except:
            return {"Success": False, "Data": response}

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
        response = None

        try:
            response = self.pedido_repository.update_pedido(
                id_pedido=id_pedido,
                id_cliente=id_cliente,
                id_produto=id_produto,
                numero_pedido=numero_pedido,
                valor=valor,
                data_pedido=data_pedido,
                status=status,
            )
            return {"Success": True, "Data": response}

        except:
            return {"Success": False, "Data": response}
