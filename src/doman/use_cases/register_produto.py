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
