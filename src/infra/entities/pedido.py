from sqlalchemy import Column, Integer, String, FLOAT
from src.infra.config import Base


class Pedido(Base):
    """Codigo Entity"""

    __tablename__ = "pedido"

    id_pedido = Column(Integer, primary_key=True)
    id_cliente = Column(Integer, nullable=False)
    id_produto = Column(Integer, nullable=False)
    numero_pedido = Column(Integer, nullable=False)
    valor = Column(FLOAT, nullable=False)
    data_pedido = Column(String, nullable=False)
    status = Column(String, nullable=False)

    def __rep__(self):
        return f"Usr [name={self.status}]"
