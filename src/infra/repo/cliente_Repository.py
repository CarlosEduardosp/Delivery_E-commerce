# pylint: disable=E1101
from typing import List
from sqlalchemy import text
from src.data.interfaces import ClienteRepositoryInterface
from src.doman.models import Cliente
from src.infra.config import DBConnectionHandler
from src.infra.entities import cliente as ClienteModels

db_connection_handler = DBConnectionHandler


class ClienteRepository(ClienteRepositoryInterface):
    """Class to manage User Repository"""

    @classmethod
    def insert_user(self, apelido: str, email: str, senha: str, cep_cliente: int) -> Cliente:
        """Insert data in user entity
        :param - apelido - person apelido
               - senha - person senha
        :return - tuple with new user inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_user = ClienteModels(apelido=apelido,
                                         email=email,
                                         senha=senha,
                                         cep_cliente=cep_cliente)
                db_connection.session.add(new_user)
                db_connection.session.commit()

                return Cliente(
                    id_cliente=new_user.id_cliente, apelido=new_user.apelido, senha=new_user.senha, cep_cliente=new_user.cep_cliente
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return None


    @classmethod
    def select_user(cls, id_cliente: int = None, apelido: str = None) -> List[Cliente]:
        """
        Select data in user entity by id and/or name
        :param - user_id: id of the registry
               - name: User name
               :return - List with Users selected
        """
        with DBConnectionHandler() as db_connection:
            try:
                query_data = None

                engine = db_connection_handler.get_engine()

                if id_cliente and not apelido:
                    with engine.connect() as connection:
                        # select data in users
                        data = connection.execute(
                            text(f"SELECT * FROM users WHERE id_cliente={id_cliente};")
                        )
                        query_data = [data]

                elif not id_cliente and apelido:
                    with engine.connect() as connection:
                        # select data in users
                        data = connection.execute(
                            text(f"SELECT * FROM users WHERE apelido={apelido};")
                        )
                        query_data = [data]

                elif id_cliente and apelido:
                    with engine.connect() as connection:
                        # select data in users
                        data = connection.execute(
                            text(
                                f"SELECT * FROM users WHERE id_cliente={id_cliente} and apelido={apelido});"
                            )
                        )
                        query_data = [data]

                return query_data

            except:
                db_connection.session.rollback()

            finally:
                db_connection.session.close()

            return None
