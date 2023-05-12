from sqlalchemy import Column, Integer
from src.infra.config import Base


class Carrinho(Base):
    """Carrinho Entity"""

    __tablename__ = "carrinho"

    id_compra = Column(Integer, primary_key=True)
    id_produto = Column(Integer, nullable=False)
    id_cliente = Column(Integer, nullable=False)

    def __rep__(self):
        return f"Usr [name={self.id_produto}]"
