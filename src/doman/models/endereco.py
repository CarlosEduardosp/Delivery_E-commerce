from collections import namedtuple

Endereco = namedtuple(
    "Endereco",
    "id_endereco cep_cliente, estado, cidade, bairro, logradouro, complemento, id_cliente",
)
