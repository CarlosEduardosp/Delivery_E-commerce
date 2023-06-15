from abc import ABC, abstractmethod
from src.doman.models import ImagemPerfil
from typing import Dict


class RegisterImagem(ABC):
    """Interface to Registerimagem Use case"""

    @abstractmethod
    def insert_imagem(self, imagem: int) -> Dict[bool, ImagemPerfil]:
        """Case"""

        raise Exception("Should implement method: registerImagemperfil")

    @abstractmethod
    def select_imagem(self) -> Dict[bool, ImagemPerfil]:
        """Case"""

        raise Exception("Should implement method: registerImagemperfil")

    @abstractmethod
    def delete_imagem(self) -> Dict[bool, ImagemPerfil]:
        """del case"""

        raise Exception("Should implement method: registerImagemperfil")
