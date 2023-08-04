from models.Base import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from sqlalchemy import ForeignKey

class Acao(Base):
    __tablename__ = 'acao'
    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    nome: Mapped[str] = mapped_column(length=100)
    ticket: Mapped[str] = mapped_column(length=10)
    valor_compra: Mapped[float]
    quantidade_compra: Mapped[int]
    data_compra: Mapped[datetime]
    cliente_id: Mapped[int] = mapped_column(ForeignKey("cliente.id"))

    def __repr__(self):
        return f"Acao(nome={self.nome}, ticket={self.ticket}, valor_compra={self.valor_compra}, " \
               f"quantidade_compra={self.quantidade_compra}, data_compra={self.data_compra}, " \
               f"cliente_id={self.cliente_id})"