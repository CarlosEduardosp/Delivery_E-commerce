from sqlalchemy import Column, String, Integer
from src.infra.config import Base


class Endereco(Base):
    """Users Entity"""

    __tablename__ = "endereco"

    id_endereco = Column(Integer, primary_key=True)
    cep_cliente = Column(String, nullable=False)
    estado = Column(String, nullable=False)
    cidade = Column(String, nullable=False)
    bairro = Column(String, nullable=False)
    logradouro = Column(String, nullable=False)
    complemento = Column(String, nullable=False)
    id_cliente = Column(Integer, nullable=False)

    def __rep__(self):
        return f"Usr [name={self.cep_cliente}]"
