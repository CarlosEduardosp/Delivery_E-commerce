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

    def select_produto(self, id_produto: int) -> Dict[bool, Produto]:
        """select produto"""

        response = None
        validate_entry = isinstance(id_produto, int)

        if validate_entry:
            response = self.produto_repository.select_produto(id_produto=id_produto)
            return {"Success": True, "Data": response}

        return {"Success": False, "Data": response}

    def select_all_produto(self) -> Dict[bool, Produto]:
        """case select all"""

        try:
            ids = []
            response = self.produto_repository.select_all_produto()
            for i in response:
                ids.append(i.id_produto)
            quantidade = len(ids)
            return {"Success": True, "Data": response, "Len": quantidade}
        except:
            return {"Success": False, "Data": None}

    def delete_produto(self, id_produto: int) -> Dict[bool, Produto]:
        """delete in case"""

        response = None
        validate_entry = isinstance(id_produto, int)

        if validate_entry:
            response = self.produto_repository.delete_produto(id_produto=id_produto)
            return {"Success": True, "Data": response}

        return {"Success": False, "Data": response}

    def update_produto(
        self, id_produto: int, nome: str, descricao: str, imagem: str, preco: float
    ) -> Dict[bool, Produto]:
        """update in produto"""

        response = None
        validade_entry = (
            isinstance(id_produto, int)
            and isinstance(nome, str)
            and isinstance(descricao, str)
            and isinstance(imagem, str)
            and isinstance(preco, float)
        )
        if validade_entry:
            response = self.produto_repository.update_produto(
                id_produto=id_produto,
                nome=nome,
                descricao=descricao,
                imagem=imagem,
                preco=preco,
            )
            return {"Success": True, "Data": response}

        return {"Success": False, "Data": response}
