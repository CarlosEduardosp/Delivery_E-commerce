# pylint: disable=E1101
from typing import List
from sqlalchemy import text
from src.infra.config import DBConnectionHandler
from src.data.interfaces import CodigoRepositoryInterface
from src.doman.models import Codigo
from src.infra.entities import Codigo as CodigoModels

db_connection_handler = DBConnectionHandler()


class CodigoRepository(CodigoRepositoryInterface):
    """Class to manage User Repository"""

    @classmethod
    def insert_codigo(self, codigo: int = None) -> Codigo:
        """Insert data in user entity
        :param - apelido - person apelido
               - senha - person senha
        :return - tuple with new user inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                if codigo:
                    new_user = CodigoModels(codigo=codigo)

                    db_connection.session.add(new_user)
                    db_connection.session.commit()

                    return Codigo(id_codigo=new_user.id_codigo, codigo=codigo)

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return None

    @classmethod
    def select_codigo(self) -> List[Codigo]:
        """
        Select data in user entity by id and/or name
        :param - id_cliente: id of the registry
               - apelido: apelido
               :return - List with Cliente selected
        """
        with DBConnectionHandler() as db_connection:
            try:
                engine = db_connection_handler.get_engine()
                """select data of select in codigo"""

                with engine.connect() as connection:
                    data = connection.execute(
                        text(f"SELECT * FROM codigo WHERE id_codigo={1} ;")
                    )
                    connection.commit()

                    return data

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
            return None

    @classmethod
    def delete_codigo(self) -> None:
        """Deleting data by id_cliente
        :param - id_cliente id of registry"""

        with DBConnectionHandler() as db_connection:
            engine = db_connection_handler.get_engine()
            try:
                """deleting data of select in codigo"""
                with engine.connect() as connection:
                    connection.execute(
                        text(f"DELETE FROM codigo WHERE id_codigo={1} ;")
                    )
                    connection.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
            return None
