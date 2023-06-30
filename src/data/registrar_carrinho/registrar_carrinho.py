from typing import Dict
from src.doman.use_cases.register_carrinho import (
    RegisterCarrinho as RegisterCarrinhoInterface,
)
from src.data.interfaces import carrinho_repository_interface as CarrinhoRepository
from src.doman.models import Carrinho


class RegisterCarrinho(RegisterCarrinhoInterface):
    """Class to define usercase: Register carrinho"""

    def __init__(self, carrinho_repository: type[CarrinhoRepository]):
        self.carrinho_repository = carrinho_repository

    def insert_carrinho(self, id_produto: int, id_cliente: int) -> Dict[bool, Carrinho]:
        """Register user use case"""

        response = None
        # validate_entry == True or False
        validade_entry = isinstance(id_produto, int) and isinstance(id_produto, int)

        if validade_entry:  # if validate_entry == True
            response = self.carrinho_repository.insert_carrinho(
                id_produto=id_produto, id_cliente=id_cliente
            )

        return {"Success": validade_entry, "Data": response}

    def select_carrinho(self, id_cliente: int) -> Dict[bool, Carrinho]:
        """select in Carrinho"""

        response = None
        validate_entry = isinstance(id_cliente, int)

        if validate_entry:
            response = self.carrinho_repository.select_carrinho(id_cliente=id_cliente)
            quantidade = len(response)

            return {"Success": True, "Data": response, "len": quantidade}

        return {"Success": False, "Data": response}

    def delete_carrinho(self, id_cliente: int, id_produto: int) -> Dict[bool, Carrinho]:
        """delete in case"""

        response = None
        validate_entry = isinstance(id_cliente, int) and isinstance(id_produto, int)

        if validate_entry:
            response = self.carrinho_repository.delete_carrinho(
                id_cliente=id_cliente, id_produto=id_produto
            )
            return {"Success": True, "Data": response}

        return {"Success": False, "Data": response}

    def select_all_carrinho(self) -> Dict[bool, Carrinho]:
        """case select all"""

        try:
            todos_os_ids = []
            response = self.carrinho_repository.select_all_carrinho()
            response_dict = []
            for i in response:
                todos_os_ids.append(i.id_cliente)
                response_dict.append(i)
            quantidade = len(todos_os_ids)

            return {"Success": True, "Data": response_dict, "Len": quantidade}
        except:
            return {"Success": False, "Data": None}
