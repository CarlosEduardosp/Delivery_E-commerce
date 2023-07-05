# pylint: disable=E1101
from typing import List
from sqlalchemy import text
from src.infra.config import DBConnectionHandler
from src.data.interfaces import ImagemPerfilRepositoryInterface
from src.doman.models import ImagemPerfil
from src.infra.entities import ImagemPerfil as ImagemPerfilModels

db_connection_handler = DBConnectionHandler()


class ImagemPerfilRepository(ImagemPerfilRepositoryInterface):
    """Class to manage imagemperfil Repository"""

    @classmethod
    def insert_imagem(self, imagem: str = None) -> ImagemPerfil:
        """Insert data in imagemperfil entity
        :param - imagem - imagem drawn
        :return - tuple with new imagem inserted
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
        Select data in imagemperfil
        :param - null
        :return - List with imagem selected
        """
        with DBConnectionHandler() as db_connection:
            try:
                engine = db_connection_handler.get_engine()
                """select data of select in Imagem"""

                with engine.connect() as connection:
                    data = connection.execute(text(f"SELECT * FROM imagemperfil;"))
                    connection.commit()

                    imagem = []
                    for i in data:
                        imagem.append(i)

                    return ImagemPerfil(
                        imagem=imagem[0].imagem, id_imagem=imagem[0].id_imagem
                    )

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
            return None

    @classmethod
    def delete_imagem(self) -> None:
        """Deleting data in imagemperfil
        :param - null"""

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
