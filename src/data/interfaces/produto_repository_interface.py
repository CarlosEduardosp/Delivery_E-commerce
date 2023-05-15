from abc import ABC, abstractmethod
from typing import List
from src.doman.models.produto import Produto


class ProdutoRepositoryInterface(ABC):

    """Interface to Produto Repository"""

    @abstractmethod
    def insert_produto(
        self,
        nome: str = None,
        descricao: str = None,
        imagem: str = None,
        preco: float = None,
    ) -> Produto:
        """Abstractmethod"""

        raise Exception("Method not implementend")

    @abstractmethod
    def select_produto(self, id_produto: int = None) -> List[Produto]:
        """Abstractmethod"""

        raise Exception("Method not implementend")

    @abstractmethod
    def delete_produto(self, id_produto: int = None) -> None:
        """Abstractmethod"""

        raise Exception("Method not implementend")

    @abstractmethod
    def update_produto(
        self,
        id_produto: int = None,
        nome: str = None,
        descricao: str = None,
        imagem: str = None,
        preco: float = None,
    ) -> List[Produto]:
        """Abstractmethod"""

        raise Exception("Method not implementend")
