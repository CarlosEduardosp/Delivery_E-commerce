from collections import namedtuple

Produto = namedtuple(
    "Produto",
    "id_produto nome, descricao, imagem, preco",
)
