# pylint: disable=E1101
# from typing import List
# from sqlalchemy import text
from src.infra.config import DBConnectionHandler
from src.data.interfaces import PedidoRepositoryInterface
from src.doman.models import Pedido
from src.infra.entities import Pedido as Pedidomodels

db_connection_handler = DBConnectionHandler()


class PedidoRepository(PedidoRepositoryInterface):
    """Class to manage User Repository"""

    @classmethod
    def insert_pedido(
        self,
        id_cliente: int = None,
        id_produto: int = None,
        numero_pedido: int = None,
        valor: float = None,
        data_pedido: str = None,
        status: str = None,
    ) -> Pedido:
        """Insert data in user entity
        :param - apelido - person apelido
               - senha - person senha
        :return - tuple with new user inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_user = Pedidomodels(
                    id_cliente=id_cliente,
                    id_produto=id_produto,
                    numero_pedido=numero_pedido,
                    valor=valor,
                    data_pedido=data_pedido,
                    status=status,
                )
                db_connection.session.add(new_user)
                db_connection.session.commit()

                return Pedido(
                    id_pedido=new_user.id_pedido,
                    id_cliente=new_user.id_cliente,
                    id_produto=new_user.id_produto,
                    numero_pedido=new_user.numero_pedido,
                    valor=new_user.valor,
                    data_pedido=new_user.data_pedido,
                    status=new_user.status,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return None
