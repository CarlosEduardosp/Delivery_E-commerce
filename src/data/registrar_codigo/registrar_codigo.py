from typing import Dict
from src.doman.use_cases.register_codigo import (
    RegisterCodigo as RegisterCodigoInterface,
)
from src.data.interfaces import CodigoRepositoryInterface as CodigoRepository
from src.doman.models import Codigo


class RegisterCodigo(RegisterCodigoInterface):
    """Class to define usercase: Register codigo"""

    def __init__(self, codigo_repository: type[CodigoRepository]):
        self.codigo_repository = codigo_repository

    def insert_codigo(self, codigo: int, id_cliente: int) -> Dict[bool, Codigo]:
        """Register codigo use case"""

        response = None
        # validate_entry == True or False
        validade_entry = isinstance(codigo, int) and isinstance(id_cliente, int)

        if validade_entry:  # if validate_entry == True
            response = self.codigo_repository.insert_codigo(
                codigo=codigo, id_cliente=id_cliente
            )

        return {"Success": validade_entry, "Data": response}

    def select_codigo(self, id_cliente: int) -> Dict[bool, Codigo]:
        """select in Codigo"""

        response = None
        validate_entry = isinstance(id_cliente, int)

        if validate_entry:
            response = self.codigo_repository.select_codigo(id_cliente=id_cliente)
            return {"Success": True, "Data": response}

        return {"Success": False, "Data": response}

    def delete_codigo(self, id_cliente: int) -> Dict[bool, Codigo]:
        """delete in case"""

        response = None
        validate_entry = isinstance(id_cliente, int)

        if validate_entry:
            response = self.codigo_repository.delete_codigo(id_cliente=id_cliente)
            return {"Success": True, "Data": response}

        return {"Success": False, "Data": response}
