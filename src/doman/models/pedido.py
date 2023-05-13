from collections import namedtuple

Pedido = namedtuple(
    "Pedido",
    "id_pedido id_cliente, id_produto, data_pedido, numero_pedido, valor, status ",
)
