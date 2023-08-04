from models.Base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey


class Endereco(Base):
    __tablename__ = 'endereco'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    cep: Mapped[str] = mapped_column(length=9)
    logradouro: Mapped[str] = mapped_column(length=100, nullable=True)
    complemento: Mapped[str] = mapped_column(length=100, nullable=True)
    bairro: Mapped[str] = mapped_column(length=100, nullable=True)
    cidade: Mapped[str] = mapped_column(length=100, nullable=False)
    estado: Mapped[str] = mapped_column(length=2, nullable=False)
    numero_residencia: Mapped[str] = mapped_column(length=10, nullable=True)
    cliente_id: Mapped[int] = mapped_column(ForeignKey("cliente.id"))

    def __repr__(self):
        return f"Endereco(cep={self.cep}, logradouro={self.logradouro}, complemento={self.complemento}," \
               f" bairro={self.bairro}, cidade={self.cidade}, estado={self.estado}," \
               f" numero_residencia={self.numero_residencia}, cliente_id={self.cliente_id})"
