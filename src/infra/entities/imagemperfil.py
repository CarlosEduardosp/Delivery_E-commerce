from sqlalchemy import Column, Integer, String
from src.infra.config import Base


class ImagemPerfil(Base):
    """Codigo Entity"""

    __tablename__ = "imagemperfil"

    id_imagem = Column(Integer, primary_key=True)
    imagem = Column(String, nullable=False)

    def __rep__(self):
        return f"Usr [name={self.imagem}]"
