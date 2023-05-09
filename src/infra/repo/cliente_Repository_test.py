# pylint: disable=E1101
from sqlalchemy import text
from src.infra.config import DBConnectionHandler
from .cliente_Repository import UserRepository

user_repostory = UserRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_cliente():
    """should insert User"""

    name = "kadu"
    password = "1234"

    try:

        # SQL comands
        new_user = user_repostory.insert_user(name, password)

        assert new_user.name == name
        assert new_user.password == password

    except:
        print('ERRO - Usuário já existe')


def select_cliente():
    """Select in users"""

    engine = db_connection_handler.get_engine()

    try:
        with engine.connect() as connection:
            # select data in users
            query_user = connection.execute(text(f"SELECT * FROM users WHERE id={3} ;"))

        for us in query_user:
            print(f"Selected id {us.id} ->", us.name)

    except:
        print("Usuario não encontrado.")


def delete_cliente():
    """deleting data in users"""

    engine = db_connection_handler.get_engine()

    """ deleting data of select in users """
    with engine.connect() as connection:
        connection.execute(text(f"DELETE FROM users WHERE id>{0} ;"))
        connection.commit()
