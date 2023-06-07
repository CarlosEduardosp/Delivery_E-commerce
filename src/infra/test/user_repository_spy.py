from typing import List
from src.doman.models import Cliente
from src.doman.test.mock_users import mock_users


class UserRepositorySpy:
    """Spy to user Repository"""

    def __init__(self):
        self.insert_user_params = {}
        self.select_user_params = {}

    def insert_cliente_spy(
        self, apelido: str, email: str, senha: str, cep_cliente: int
    ) -> Cliente:
        """Spy to all the attributes"""

        self.insert_user_params["apelido"] = apelido
        self.insert_user_params["email"] = email
        self.insert_user_params["senha"] = senha
        self.insert_user_params["cep_cliente"] = cep_cliente

        return mock_users()

    def select_user_spy(self, id_cliente: int = None) -> List[Cliente]:
        """Spy to all the attributes"""

        self.select_user_params["id_cliente"] = id_cliente

        return [mock_users()]
