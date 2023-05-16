from sqlalchemy import Column, Integer
from src.infra.config import Base


class Codigo(Base):
    """Codigo Entity"""

    __tablename__ = "codigo"

    id_codigo = Column(Integer, primary_key=True)
    id_cliente = Column(Integer, nullable=False)
    codigo = Column(Integer, nullable=False)

    def __rep__(self):
        return f"Usr [name={self.codigo}]"
