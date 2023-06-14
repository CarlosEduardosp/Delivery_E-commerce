from typing import Dict
from src.doman.use_cases.register_endereco import (
    RegisterEndereco as RegisterEnderecoInterface,
)
from src.data.interfaces import endereco_repository_interface as enderecorepository
from src.doman.models import Endereco


class RegisterEndereco(RegisterEnderecoInterface):
    """Class to define usercase: Register User"""

    def __init__(self, endereco_repository: type[enderecorepository]):
        self.endereco_repository = endereco_repository

    def insert_endereco(
        self,
        cep_cliente: str,
        estado: str,
        cidade: str,
        bairro: str,
        logradouro: str,
        complemento: str,
        id_cliente: int,
    ) -> Dict[bool, Endereco]:
        """Register user use case
        :param - name: person name
               - password: person password
        :return - Dictionary with informations of the process
        """

        response = None
        # validate_entry == True or False
        validade_entry = (
            isinstance(cep_cliente, str)
            and isinstance(estado, str)
            and isinstance(cidade, str)
            and isinstance(bairro, str)
            and isinstance(logradouro, str)
            and isinstance(complemento, str)
            and isinstance(id_cliente, int)
        )

        if validade_entry:  # if validate_entry == True
            response = self.endereco_repository.insert_endereco(
                cep_cliente, estado, cidade, bairro, logradouro, complemento, id_cliente
            )

        return {"Success": validade_entry, "Data": response}

    def select_endereco(self, id_cliente: int) -> Dict[bool, Endereco]:
        """select in Cliente"""

        response = None
        validate_entry = isinstance(id_cliente, int)

        if validate_entry:
            response = self.endereco_repository.select_endereco(id_cliente=id_cliente)
            return {"Success": True, "Data": response}

        return {"Success": False, "Data": response}

    def delete_endereco(self, id_cliente: int) -> Dict[bool, Endereco]:
        """delete in case"""

        response = None
        validate_entry = isinstance(id_cliente, int)

        if validate_entry:
            response = self.endereco_repository.delete_endereco(id_cliente=id_cliente)
            return {"Success": True, "Data": response}

        return {"Success": False, "Data": response}

    def select_all_endereco(self) -> Dict[bool, Endereco]:
        """case select all"""

        try:
            ids = []
            response = self.endereco_repository.select_all_endereco()
            for i in response:
                ids.append(i.id_cliente)
            quantidade = len(ids)
            return {"Success": True, "Data": response, "Len": quantidade}
        except:
            return {"Success": False, "Data": None}

    def update_endereco(
        self,
        id_endereco: int,
        cep_cliente: str,
        estado: str,
        cidade: str,
        bairro: str,
        logradouro: str,
        complemento: str,
        id_cliente: int,
    ) -> Dict[bool, Endereco]:
        """update in endereco"""

        response = None
        validade_entry = (
            isinstance(id_endereco, int)
            and isinstance(cep_cliente, str)
            and isinstance(estado, str)
            and isinstance(cidade, str)
            and isinstance(bairro, str)
            and isinstance(logradouro, str)
            and isinstance(complemento, str)
            and isinstance(id_cliente, int)
        )

        if validade_entry:
            self.endereco_repository.update_endereco(
                id_endereco=id_endereco,
                cep_cliente=cep_cliente,
                estado=estado,
                cidade=cidade,
                bairro=bairro,
                logradouro=logradouro,
                complemento=complemento,
                id_cliente=id_cliente,
            )

            return {"Success": True, "Data": response}

        return {"Success": False, "Data": response}
