from abc import ABC, abstractmethod
from src.doman.models import Produto
from typing import Dict


class RegisterProduto(ABC):
    """Interface to RegisterProduto Use case"""

    @abstractmethod
    def register(
        self, nome: str, descricao: str, imagem: str, preco: float
    ) -> Dict[bool, Produto]:
        """Case"""

        raise Exception("Should implement method: register")

    @abstractmethod
    def select_all_produto(self) -> Dict[bool, Produto]:
        """case select all produto"""

        raise Exception("Should implement method: register")

    @abstractmethod
    def select_produto(self, id_produto: int) -> Dict[bool, Produto]:
        """Case"""

        raise Exception("Should implement method: register")

    @abstractmethod
    def delete_produto(self, id_produto: int) -> Dict[bool, Produto]:
        """delete in case"""

        raise Exception("Should implement method: register")

    @abstractmethod
    def update_produto(
        self, id_produto: int, nome: str, descricao: str, imagem: str, preco: float
    ) -> Dict[bool, Produto]:
        raise Exception("Should implement method: register")
