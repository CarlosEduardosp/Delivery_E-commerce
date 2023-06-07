from typing import Dict
from src.doman.use_cases.register_produto import (
    RegisterProduto as RegisterProdutoInterface,
)
from src.data.interfaces import produto_repository_interface as produtorepository
from src.doman.models import Produto


class RegisterProduto(RegisterProdutoInterface):
    """Class to define usercase: Register User"""

    def __init__(self, produto_repository: type[produtorepository]):
        self.produto_repository = produto_repository

    def register(
        self, nome: str, descricao: str, imagem: str, preco: float
    ) -> Dict[bool, Produto]:
        """Register produto use case"""

        response = None
        # validate_entry == True or False
        validade_entry = (
            isinstance(nome, str)
            and isinstance(descricao, str)
            and isinstance(imagem, str)
            and isinstance(preco, float)
            and (len(nome) > 3)
            and (preco > 0)
        )

        if validade_entry:  # if validate_entry == True
            response = self.produto_repository.insert_produto(
                nome=nome, descricao=descricao, imagem=imagem, preco=preco
            )

        return {"Success": validade_entry, "Data": response}
