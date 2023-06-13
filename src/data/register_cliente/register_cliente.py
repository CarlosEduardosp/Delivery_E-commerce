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
        self, apelido: str, email: str, senha: str, cep_cliente: int
    ) -> Dict[bool, Cliente]:
        """Register user use case
        :param - name: person name
               - password: person password
        :return - Dictionary with informations of the process
        """

        response = None
        # validate_entry == True or False
        validade_entry = (
            isinstance(apelido, str)
            and isinstance(email, str)
            and isinstance(senha, str)
            and isinstance(cep_cliente, int)
        )

        if validade_entry:  # if validate_entry == True
            response = self.cliente_repository.insert_cliente(
                apelido, email, senha, cep_cliente
            )

        return {"Success": validade_entry, "Data": response}

    def select_cliente(self, id_cliente: int) -> Dict[bool, Cliente]:
        """select in Cliente"""

        response = None
        validate_entry = isinstance(id_cliente, int)

        if validate_entry:
            response = self.cliente_repository.select_cliente(id_cliente=id_cliente)
            return {"Success": True, "Data": response}

        return {"Success": False, "Data": response}

    def delete_cliente(self, id_cliente: int) -> Dict[bool, Cliente]:
        """delete in case"""

        response = None
        validate_entry = isinstance(id_cliente, int)

        if validate_entry:
            response = self.cliente_repository.delete_cliente(id_cliente=id_cliente)
            return {"Success": True, "Data": response}

        return {"Success": False, "Data": response}

    def select_all_cliente(self) -> Dict[bool, Cliente]:
        """case select all"""

        try:
            ids = []
            response = self.cliente_repository.select_all_cliente()
            for i in response:
                ids.append(i.id_cliente)
            quantidade = len(ids)
            return {"Success": True, "Data": response, "Len": quantidade}
        except:
            return {"Success": False, "Data": None}

    def update_cliente(
        self, id_cliente: int, apelido: str, email: str, senha: str, cep_cliente: str
    ) -> Dict[bool, Cliente]:
        """update in Cliente"""

        response = None
        validade_entry = (
            isinstance(id_cliente, int)
            and isinstance(apelido, str)
            and isinstance(senha, str)
            and isinstance(email, str)
            and isinstance(cep_cliente, str)
        )
        if validade_entry:
            response = self.cliente_repository.update_cliente(
                id_cliente=id_cliente,
                apelido=apelido,
                senha=senha,
                email=email,
                cep_cliente=cep_cliente,
            )
            return {"Success": True, "Data": response}

        return {"Success": False, "Data": response}
