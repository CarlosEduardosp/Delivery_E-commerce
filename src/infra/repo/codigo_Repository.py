# pylint: disable=E1101
from typing import List
from sqlalchemy import text
from src.infra.config import DBConnectionHandler
from src.data.interfaces import CodigoRepositoryInterface
from src.doman.models import Codigo
from src.infra.entities import Codigo as CodigoModels

db_connection_handler = DBConnectionHandler()


class CodigoRepository(CodigoRepositoryInterface):
    """Class to manage codigo Repository"""

    @classmethod
    def insert_codigo(self, codigo: int = None, id_cliente: int = None) -> Codigo:
        """Insert data in codigo entity
        :param - codigo - codigo drawn
        :return - tuple with new codigo inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                if codigo:
                    new_user = CodigoModels(codigo=codigo, id_cliente=id_cliente)

                    db_connection.session.add(new_user)
                    db_connection.session.commit()

                    return Codigo(
                        id_codigo=new_user.id_codigo,
                        codigo=new_user.codigo,
                        id_cliente=new_user.id_cliente,
                    )

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return None

    @classmethod
    def select_codigo(self, id_cliente: int = None) -> List[Codigo]:
        """
        Select data in codigo entity by id
        :param - id_cliente: id of the registry
               :return - List with Codigo selected
        """
        with DBConnectionHandler() as db_connection:
            try:
                engine = db_connection_handler.get_engine()
                """select data of select in codigo"""

                with engine.connect() as connection:
                    data = connection.execute(
                        text(f"SELECT * FROM codigo WHERE id_cliente={id_cliente} ;")
                    )
                    connection.commit()

                    codigo = []
                    for i in data:
                        codigo.append(i)

                    return Codigo(
                        codigo=codigo[0].codigo,
                        id_cliente=codigo[0].id_cliente,
                        id_codigo=codigo[0].id_codigo,
                    )

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
            return None

    @classmethod
    def delete_codigo(self, id_cliente: int = None) -> None:
        """Deleting data by id_cliente
        :param - id_cliente id of registry"""

        with DBConnectionHandler() as db_connection:
            engine = db_connection_handler.get_engine()
            try:
                """deleting data of select in codigo"""
                with engine.connect() as connection:
                    connection.execute(
                        text(f"DELETE FROM codigo WHERE id_cliente={id_cliente} ;")
                    )
                    connection.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
            return None
