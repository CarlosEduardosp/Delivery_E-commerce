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
            response = self.cliente_repository.insert_cliente_spy(
                apelido, email, senha, cep_cliente
            )

        return {"Success": validade_entry, "Data": response}
