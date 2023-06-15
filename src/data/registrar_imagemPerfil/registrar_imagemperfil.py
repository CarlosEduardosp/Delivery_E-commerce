from typing import Dict
from src.doman.use_cases.register_imagemperfil import (
    RegisterImagem as RegisterImagemInterface,
)
from src.data.interfaces import ImagemPerfilRepositoryInterface as ImagemRepository
from src.doman.models import ImagemPerfil


class RegisterImagemperfil(RegisterImagemInterface):
    """Class to define usercase: Register imagem"""

    def __init__(self, imagemperfil_repository: type[ImagemRepository]):
        self.imagemperfil_repository = imagemperfil_repository

    def insert_imagem(self, imagem: str) -> Dict[bool, ImagemPerfil]:
        """Register imagem use case"""

        response = None
        # validate_entry == True or False
        validade_entry = isinstance(imagem, str)

        if validade_entry:  # if validate_entry == True
            response = self.imagemperfil_repository.insert_imagem(imagem=imagem)

        return {"Success": validade_entry, "Data": response}

    def select_imagem(self) -> Dict[bool, ImagemPerfil]:
        """select in Imagem"""

        response = self.imagemperfil_repository.select_imagem()
        return {"Success": True, "Data": response}

    def delete_imagem(self) -> Dict[bool, ImagemPerfil]:
        """delete in case"""

        response = self.imagemperfil_repository.delete_imagem()
        return {"Success": True, "Data": response}
