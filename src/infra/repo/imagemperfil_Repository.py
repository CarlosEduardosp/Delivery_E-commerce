# pylint: disable=E1101
from typing import List
from sqlalchemy import text
from src.infra.config import DBConnectionHandler
from src.data.interfaces import ImagemPerfilRepositoryInterface
from src.doman.models import ImagemPerfil
from src.infra.entities import ImagemPerfil as ImagemPerfilModels

db_connection_handler = DBConnectionHandler()


class ImagemPerfilRepository(ImagemPerfilRepositoryInterface):
    """Class to manage User Repository"""

    @classmethod
    def insert_imagem(self, imagem: str = None) -> ImagemPerfil:
        """Insert data in user entity
        :param - apelido - person apelido
               - senha - person senha
        :return - tuple with new user inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                if imagem:
                    new_user = ImagemPerfilModels(imagem=imagem)

                    db_connection.session.add(new_user)
                    db_connection.session.commit()

                    return ImagemPerfil(id_imagem=new_user.id_imagem, imagem=imagem)

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return None

    @classmethod
    def select_imagem(self) -> List[ImagemPerfil]:
        """
        Select data in user entity by id and/or name
        :param - id_cliente: id of the registry
               - apelido: apelido
               :return - List with Cliente selected
        """
        with DBConnectionHandler() as db_connection:
            try:
                engine = db_connection_handler.get_engine()
                """select data of select in Imagem"""

                with engine.connect() as connection:
                    data = connection.execute(text(f"SELECT * FROM codigo;"))
                    connection.commit()

                    return data

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
            return None

    @classmethod
    def delete_imagem(self) -> None:
        """Deleting data by id_cliente
        :param - id_cliente id of registry"""

        with DBConnectionHandler() as db_connection:
            engine = db_connection_handler.get_engine()
            try:
                """deleting data of select in imagemperfil"""
                with engine.connect() as connection:
                    connection.execute(
                        text(f"DELETE FROM imagemperfil WHERE id_imagem={1} ;")
                    )
                    connection.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
            return None
