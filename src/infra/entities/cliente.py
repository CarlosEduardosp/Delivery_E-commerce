from sqlalchemy import Column, String, Integer
from src.infra.config import Base


class Cliente(Base):
    """Users Entity"""

    __tablename__ = "cliente"

    id_cliente = Column(Integer, primary_key=True)
    apelido = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    senha = Column(String, nullable=False)
    cep_cliente = Column(Integer, nullable=False)

    def __rep__(self):
        return f"Usr [name={self.apelido}]"
