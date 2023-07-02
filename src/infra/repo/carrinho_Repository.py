# pylint: disable=E1101
from typing import List
from sqlalchemy import text
from src.infra.config import DBConnectionHandler
from src.data.interfaces import CarrinhoRepositoryInterface
from src.doman.models import Carrinho
from src.infra.entities import Carrinho as CarrinhoModels

db_connection_handler = DBConnectionHandler()


class CarrinhoRepository(CarrinhoRepositoryInterface):
    """Class to manage carrinho Repository"""

    @classmethod
    def insert_carrinho(
        self, id_produto: int = None, id_cliente: int = None
    ) -> Carrinho:
        """Insert data in carrinho entity
        :param - id_produto
               - id_cliente
        :return - tuple with new cliente inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_user = CarrinhoModels(id_produto=id_produto, id_cliente=id_cliente)

                db_connection.session.add(new_user)
                db_connection.session.commit()

                return Carrinho(
                    id_compra=new_user.id_compra,
                    id_produto=new_user.id_produto,
                    id_cliente=new_user.id_cliente,
                )

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return None

    @classmethod
    def select_carrinho(self, id_cliente: int = None) -> List[Carrinho]:
        """
        Select data in carrinho entity by id
        :param - id_cliente: id of the registry
        :return - List with Cliente selected
        """
        with DBConnectionHandler() as db_connection:
            try:
                engine = db_connection_handler.get_engine()

                if id_cliente:
                    """select data of select in carrinho"""
                    with engine.connect() as connection:
                        data = connection.execute(
                            text(
                                f"SELECT * FROM carrinho WHERE id_cliente={id_cliente} ;"
                            )
                        )
                        connection.commit()

                        carrinho = []
                        for i in data:
                            carrinho.append(i)

                        return carrinho
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
    def select_all_carrinho(self) -> List[Carrinho]:
        """select all carrinho"""

        with DBConnectionHandler() as db_connection:
            try:
                engine = db_connection_handler.get_engine()

                with engine.connect() as connection:
                    data = connection.execute(text(f"SELECT * FROM carrinho ;"))
                    connection.commit()

                    carrinho = []
                    for i in data:
                        carrinho.append(i)

                    return carrinho

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
            return None

    @classmethod
    def delete_carrinho(self, id_cliente: int = None, id_produto: int = None) -> None:
        """Deleting data by id_cliente
        :param - id_cliente id of registry"""

        with DBConnectionHandler() as db_connection:
            engine = db_connection_handler.get_engine()
            try:
                if id_cliente:
                    """deleting data of select in carrinho"""
                    with engine.connect() as connection:
                        connection.execute(
                            text(
                                f"DELETE FROM carrinho WHERE id_produto = {id_produto} AND id_cliente = {id_cliente};"
                            )
                        )

                        connection.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
            return None
