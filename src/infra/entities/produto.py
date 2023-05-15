from sqlalchemy import Column, String, Integer, FLOAT
from src.infra.config import Base


class Produto(Base):
    """Users Entity"""

    __tablename__ = "produto"

    id_produto = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False, unique=True)
    descricao = Column(String, nullable=False, unique=True)
    imagem = Column(String, nullable=False)
    preco = Column(FLOAT, nullable=False)

    def __rep__(self):
        return f"Usr [name={self.nome}]"
