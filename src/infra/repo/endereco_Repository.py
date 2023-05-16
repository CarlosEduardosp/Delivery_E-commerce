# pylint: disable=E1101
from typing import List
from sqlalchemy import text
from src.infra.config import DBConnectionHandler
from src.data.interfaces import EnderecoRepositoryInterface
from src.doman.models import Endereco
from src.infra.entities import Endereco as EnderecoModels

db_connection_handler = DBConnectionHandler()


class EnderecoRepository(EnderecoRepositoryInterface):
    """Class to manage Endereco Repository"""

    @classmethod
    def insert_endereco(
        self,
        cep_cliente: str = None,
        estado: str = None,
        cidade: str = None,
        bairro: str = None,
        logradouro: str = None,
        complemento: str = None,
        id_cliente: int = None,
    ) -> Endereco:
        """Insert data in endereco entity"""

        with DBConnectionHandler() as db_connection:
            try:
                new_end = EnderecoModels(
                    cep_cliente=cep_cliente,
                    estado=estado,
                    cidade=cidade,
                    bairro=bairro,
                    logradouro=logradouro,
                    complemento=complemento,
                    id_cliente=id_cliente,
                )
                db_connection.session.add(new_end)
                db_connection.session.commit()

                return Endereco(
                    id_endereco=new_end.id_endereco,
                    cep_cliente=new_end.cep_cliente,
                    estado=new_end.estado,
                    cidade=new_end.cidade,
                    bairro=new_end.bairro,
                    logradouro=new_end.logradouro,
                    complemento=new_end.complemento,
                    id_cliente=new_end.id_cliente,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return None

    @classmethod
    def select_endereco(self, id_cliente: int = None) -> List[Endereco]:
        """
        Select data in endereco entity by id a
        :param - id_cliente: id of the registry
               :return - List with Endereco selected
        """
        with DBConnectionHandler() as db_connection:
            try:
                engine = db_connection_handler.get_engine()

                if id_cliente:
                    """select data of select in endereco"""
                    with engine.connect() as connection:
                        data = connection.execute(
                            text(
                                f"SELECT * FROM endereco WHERE id_cliente={id_cliente} ;"
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
    def delete_endereco(self, id_cliente: int = None) -> None:
        """Deleting data by id_cliente
        :param - id_cliente id of registry"""

        with DBConnectionHandler() as db_connection:
            engine = db_connection_handler.get_engine()
            try:
                if id_cliente:
                    """deleting data of select in endereco"""
                    with engine.connect() as connection:
                        connection.execute(
                            text(
                                f"DELETE FROM endereco WHERE id_cliente={id_cliente} ;"
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
    def update_endereco(
        self,
        cep_cliente: str = None,
        estado: str = None,
        cidade: str = None,
        bairro: str = None,
        logradouro: str = None,
        complemento: str = None,
        id_cliente: int = None,
    ) -> List[Endereco]:
        """update of endereco"""

        with DBConnectionHandler() as db_connection:
            engine = db_connection_handler.get_engine()
            try:
                if id_cliente:
                    """update data of select in endereco"""

                    with engine.connect() as connection:
                        connection.execute(
                            text(
                                f"UPDATE endereco SET id_cliente= {id_cliente}, "
                                f"cep_cliente= '{cep_cliente}',"
                                f"estado= '{estado}', "
                                f"cidade= '{cidade}', "
                                f"bairro= '{bairro}', "
                                f"logradouro= '{logradouro}', "
                                f"complemento= '{complemento}'"
                                f"WHERE id_cliente= '{id_cliente}'"
                            )
                        )

                        connection.commit()

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
            return None
