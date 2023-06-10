# pylint: disable=E1101
from typing import List
from sqlalchemy import text
from src.infra.config import DBConnectionHandler
from src.data.interfaces import ClienteRepositoryInterface
from src.doman.models import Cliente
from src.infra.entities import Cliente as ClienteModels

db_connection_handler = DBConnectionHandler()


class ClienteRepository(ClienteRepositoryInterface):
    """Class to manage Cliente Repository"""

    @classmethod
    def insert_cliente(
        self, apelido: str, email: str, senha: str, cep_cliente: int
    ) -> Cliente:
        """Insert data in user entity
        :param - apelido - person apelido
               - email - person email
               - senha - person senha
               - cep_cliente - person cep
        :return - tuple with new Cliente inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_user = ClienteModels(
                    apelido=apelido, email=email, senha=senha, cep_cliente=cep_cliente
                )
                db_connection.session.add(new_user)
                db_connection.session.commit()

                return Cliente(
                    id_cliente=new_user.id_cliente,
                    apelido=new_user.apelido,
                    email=new_user.email,
                    senha=new_user.senha,
                    cep_cliente=new_user.cep_cliente,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return None

    @classmethod
    def select_cliente(self, id_cliente: int = None) -> List[Cliente]:
        """
        Select data in cliente entity by id
        :param - id_cliente: id of the registry
               :return - List with Cliente selected
        """
        with DBConnectionHandler() as db_connection:
            try:
                engine = db_connection_handler.get_engine()

                if id_cliente:
                    """select data of select in cliente"""
                    with engine.connect() as connection:
                        data = connection.execute(
                            text(
                                f"SELECT * FROM cliente WHERE id_cliente={id_cliente} ;"
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
    def delete_cliente(self, id_cliente: int = None) -> None:
        """Deleting data by id_cliente
        :param - id_cliente id of registry"""

        with DBConnectionHandler() as db_connection:
            engine = db_connection_handler.get_engine()
            try:
                if id_cliente:
                    """deleting data of select in cliente"""
                    with engine.connect() as connection:
                        connection.execute(
                            text(f"DELETE FROM cliente WHERE id_cliente={id_cliente} ;")
                        )
                        connection.commit()

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
            return None

    @classmethod
    def update_cliente(
        self,
        id_cliente: int = None,
        apelido: str = None,
        email: str = None,
        senha: str = None,
        cep_cliente: str = None,
    ) -> List[Cliente]:
        """update of clientes"""

        with DBConnectionHandler() as db_connection:
            engine = db_connection_handler.get_engine()
            try:
                if id_cliente:
                    """update data of select in cliente"""

                    with engine.connect() as connection:
                        connection.execute(
                            text(
                                f"UPDATE cliente SET id_cliente= {id_cliente}, "
                                f"apelido= '{apelido}', "
                                f"email= '{email}', "
                                f"senha= '{senha}', "
                                f"cep_cliente= '{cep_cliente}' "
                                f"WHERE id_cliente= {id_cliente}"
                            )
                        )

                        connection.commit()

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
            return None
