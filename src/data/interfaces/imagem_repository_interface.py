from abc import ABC, abstractmethod
from typing import List
from src.doman.models.imagemperfil import ImagemPerfil


class ImagemPerfilRepositoryInterface(ABC):

    """Interface to Pet Repository"""

    @abstractmethod
    def insert_imagem(self, imagem: str = None) -> ImagemPerfil:
        """Abstractmethod"""

        raise Exception("Method not implementend")

    @abstractmethod
    def select_imagem(self) -> List[ImagemPerfil]:
        """Abstractmethod"""

        raise Exception("Method not implementend")

    @abstractmethod
    def delete_imagem(self) -> None:
        """Abstractmethod"""

        raise Exception("Method not implementend")
