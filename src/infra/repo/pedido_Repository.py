# pylint: disable=E1101
from typing import List
from sqlalchemy import text
from src.infra.config import DBConnectionHandler
from src.data.interfaces import PedidoRepositoryInterface
from src.doman.models import Pedido
from src.infra.entities import Pedido as Pedidomodels

db_connection_handler = DBConnectionHandler()


class PedidoRepository(PedidoRepositoryInterface):
    """Class to manage Produto Repository"""

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
        """Insert data in produto entity
        :param - id_cliente
               - id_produto
               - numero_ppedido
               - valor
               - data_pedido
               - status
        :return - tuple with new pedido inserted
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

    @classmethod
    def select_pedido(
        self, id_pedido: int = None, id_cliente: int = None
    ) -> List[Pedido]:
        """
        Select data in pedido entity by id_cliente and id_pedido
        :param - id_cliente: id of the registry
               - id_pedido: id of the registry
        :return - List with Pedido selected
        """
        with DBConnectionHandler() as db_connection:
            try:
                engine = db_connection_handler.get_engine()

                if id_pedido:
                    """select data of select in Pedido"""
                    with engine.connect() as connection:
                        data = connection.execute(
                            text(
                                f"SELECT * FROM pedido WHERE id_pedido={id_pedido} and id_cliente={id_cliente};"
                            )
                        )
                        connection.commit()

                        return data
                else:
                    data = None
                    return data

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
            return None

    @classmethod
    def delete_pedido(self, id_pedido: int = None, id_cliente: int = None) -> None:
        """Deleting data by id_cliente
        :param - id_cliente id of registry"""

        with DBConnectionHandler() as db_connection:
            engine = db_connection_handler.get_engine()
            try:
                if id_pedido:
                    """deleting data of select in pedido"""
                    with engine.connect() as connection:
                        connection.execute(
                            text(
                                f"DELETE FROM pedido WHERE id_pedido={id_pedido} and id_cliente={id_cliente} ;"
                            )
                        )
                        connection.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
            return None

    @classmethod
    def update_pedido(
        self,
        id_pedido: int = None,
        id_cliente: int = None,
        id_produto: int = None,
        numero_pedido: int = None,
        valor: float = None,
        data_pedido: str = None,
        status: str = None,
    ) -> List[Pedido]:
        """update of Pedido"""

        with DBConnectionHandler() as db_connection:
            engine = db_connection_handler.get_engine()
            try:
                if id_pedido:
                    """update data of select in pedido"""

                    with engine.connect() as connection:
                        connection.execute(
                            text(
                                f"UPDATE pedido SET id_pedido= {id_pedido}, "
                                f"id_cliente= '{id_cliente}', "
                                f"id_produto= '{id_produto}', "
                                f"numero_pedido= '{numero_pedido}', "
                                f"valor= '{valor}', "
                                f"data_pedido= '{data_pedido}',"
                                f"status= '{status}'"
                                f"WHERE id_pedido= {id_pedido}"
                            )
                        )

                        connection.commit()

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
            return None
