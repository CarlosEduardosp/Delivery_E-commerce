# pylint: disable=E1101
from sqlalchemy import text
from src.infra.config import DBConnectionHandler
from .cliente_Repository import ClienteRepository

cliente_repostory = ClienteRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_cliente():
    """should insert User"""

    apelido = "carol"
    senha = "0000"
    email = "carol.spadilha@yahoo.com.br"
    cep_cliente = '28984351'

    try:

        # SQL comands
        new_cliente = cliente_repostory.insert_user(apelido, email, senha, cep_cliente)



    except:
        print('ERRO - Usuário já existe')
    finally:
        print('Ok')


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
