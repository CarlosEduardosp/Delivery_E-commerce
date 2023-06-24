from typing import Dict
from src.doman.use_cases.register_cliente import (
    RegisterCliente as RegisterClienteInterface,
)
from src.data.interfaces import cliente_repository_interface as clienterepository
from src.doman.models import Cliente


class RegisterCliente(RegisterClienteInterface):
    """Class to define usercase: Register User"""

    def __init__(self, cliente_repository: type[clienterepository]):
        self.cliente_repository = cliente_repository

    def register(
        self, apelido: str, email: str, senha: str, cep_cliente: str
    ) -> Dict[bool, Cliente]:
        """Register user use case
        :param - name: person name
               - password: person password
        :return - Dictionary with informations of the process
        """

        response = None

        validade_entry = self.__validar_dados(
            apelido=apelido, email=email, senha=senha, cep_cliente=cep_cliente
        )  # validando com metodo privado.

        if validade_entry:  # if validate_entry == True
            response = self.cliente_repository.insert_cliente(
                apelido, email, senha, cep_cliente
            )
            return {"Success": True, "Data": response}

        return self.__error()

    def select_cliente(self, id_cliente: int) -> Dict[bool, Cliente]:
        """select in Cliente"""

        response = None
        validade_entry = self.__validar_dados(
            id_cliente=id_cliente
        )  # validando com metodo privado.

        if validade_entry:
            response = self.cliente_repository.select_cliente(id_cliente=id_cliente)

            return {"Success": True, "Data": response}

        return self.__error()

    def delete_cliente(self, id_cliente: int) -> Dict[bool, Cliente]:
        """delete in case"""

        response = None
        validade_entry = self.__validar_dados(
            id_cliente=id_cliente
        )  # validando com metodo privado.

        if validade_entry:
            response = self.cliente_repository.delete_cliente(id_cliente=id_cliente)
            return {"Success": True, "Data": response}

        return self.__error()

    def select_all_cliente(self) -> Dict[bool, Cliente]:
        """case select all"""

        try:
            todos_os_ids = []
            response = self.cliente_repository.select_all_cliente()
            response_dict = []
            for i in response:
                todos_os_ids.append(i.id_cliente)
                response_dict.append(i)
            quantidade = len(todos_os_ids)

            return {"Success": True, "Data": response_dict, "Len": quantidade}
        except:
            return self.__error()

    def update_cliente(
        self, id_cliente: int, apelido: str, email: str, senha: str, cep_cliente: str
    ) -> Dict[bool, Cliente]:
        """update in Cliente"""

        response = None
        validade_entry = self.__validar_dados(
            apelido=apelido,
            id_cliente=id_cliente,
            email=email,
            senha=senha,
            cep_cliente=cep_cliente,
        )  # validando com metodo privado.

        if validade_entry:
            response = self.cliente_repository.update_cliente(
                id_cliente=id_cliente,
                apelido=apelido,
                senha=senha,
                email=email,
                cep_cliente=cep_cliente,
            )
            return {"Success": True, "Data": response}

        return self.__error(response)

    def __validar_dados(
        self,
        id_cliente: int = 0,
        apelido: str = "",
        email: str = "@",
        senha: str = "",
        cep_cliente: str = "",
    ) -> bool:
        """Validador de dados"""

        if not isinstance(id_cliente, int):
            raise ValueError("id_cliente deve ser um número inteiro")

        if not isinstance(apelido, str):
            raise ValueError("apelido deve ser uma string")

        if not isinstance(email, str):
            raise ValueError("email deve ser uma string")

        if "@" not in email:
            raise ValueError("Email Inválido - sem o caracter '@'")

        if not isinstance(senha, str):
            raise ValueError("senha deve ser uma string")

        if not isinstance(cep_cliente, str):
            raise ValueError("cep_cliente deve ser uma string ou None")

        return True

    def __error(self, response: str = None):
        """mensagem de erro"""

        return {"Success": False, "Data": response}
