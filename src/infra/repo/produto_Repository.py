# pylint: disable=E1101
from typing import List
from sqlalchemy import text
from src.infra.config import DBConnectionHandler
from src.data.interfaces import ProdutoRepositoryInterface
from src.doman.models import Produto
from src.infra.entities import Produto as Produtomodels

db_connection_handler = DBConnectionHandler()


class ProdutoRepository(ProdutoRepositoryInterface):
    """Class to manage Produto Repository"""

    @classmethod
    def insert_produto(
        self,
        nome: str = None,
        descricao: str = None,
        imagem: str = None,
        preco: str = None,
    ) -> Produto:
        """Insert data in produto entity
        :param - nome - product name
               - descricao - product description
               - imagem - product image
        :return - tuple with new produto inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_user = Produtomodels(
                    nome=nome,
                    descricao=descricao,
                    imagem=imagem,
                    preco=preco,
                )
                db_connection.session.add(new_user)
                db_connection.session.commit()

                return Produto(
                    id_produto=new_user.id_produto,
                    nome=new_user.nome,
                    descricao=new_user.descricao,
                    imagem=new_user.imagem,
                    preco=new_user.preco,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return None

    @classmethod
    def select_produto(self, id_produto: int = None) -> List[Produto]:
        """
        Select data in produto entity by id and
        :param - id_produto: id of the registry
        :return - List with produto selected
        """
        with DBConnectionHandler() as db_connection:
            try:
                engine = db_connection_handler.get_engine()

                if id_produto:
                    """select data of select in produto"""
                    with engine.connect() as connection:
                        data = connection.execute(
                            text(
                                f"SELECT * FROM produto WHERE id_produto={id_produto} ;"
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
    def delete_produto(self, id_produto: int = None) -> None:
        """Deleting data by id_produto
        :param - id_produto id of registry"""

        with DBConnectionHandler() as db_connection:
            engine = db_connection_handler.get_engine()
            try:
                if id_produto:
                    """deleting data of select in produto"""
                    with engine.connect() as connection:
                        connection.execute(
                            text(f"DELETE FROM produto WHERE id_produto={id_produto} ;")
                        )
                        connection.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
            return None

    @classmethod
    def update_produto(
        self,
        id_produto: int = None,
        nome: str = None,
        descricao: str = None,
        imagem: str = None,
        preco: float = None,
    ) -> List[Produto]:
        """update of products"""

        with DBConnectionHandler() as db_connection:
            engine = db_connection_handler.get_engine()
            try:
                if id_produto:
                    """update data of select in produto"""

                    with engine.connect() as connection:
                        connection.execute(
                            text(
                                f"UPDATE produto SET id_produto= {id_produto}, "
                                f"nome= '{nome}', "
                                f"descricao= '{descricao}', "
                                f"imagem= '{imagem}', "
                                f"preco= '{preco}' "
                                f"WHERE id_produto= {id_produto}"
                            )
                        )

                        connection.commit()

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
            return None
