from abc import ABC, abstractmethod
from src.doman.models_class_routes.endereco_cep_cliente import Endereco


class BuscarCepInterface(ABC):
    """Interface to buscarcep Use case"""

    @abstractmethod
    def pesquisar_cep(self, cep_cliente) -> Endereco:
        """Case"""

        raise Exception("Should implement method: register")
