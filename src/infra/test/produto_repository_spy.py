from typing import List
from src.doman.models import Produto
from src.doman.test.mock_products import mock_products


class ProdutoRepositorySpy:
    """Spy to user Repository"""

    def __init__(self):
        self.insert_produto_params = {}
        self.select_produto_params = {}

    def insert_produto_spy(
        self, nome: str, descricao: str, imagem: str, preco: int
    ) -> Produto:
        """Spy to all the attributes"""

        self.insert_produto_params["nome"] = nome
        self.insert_produto_params["descricao"] = descricao
        self.insert_produto_params["imagem"] = imagem
        self.insert_produto_params["preco"] = preco

        return mock_products()

    def select_produto_spy(self, id_produto: int = None) -> List[Produto]:
        """Spy to all the attributes"""

        self.select_produto_params["id_produto"] = id_produto

        return [mock_products()]
