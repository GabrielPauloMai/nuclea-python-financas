from models.Base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


class Endereco(Base):
    __tablename__ = 'endereco'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    cep: Mapped[str]
    logradouro: Mapped[str]
    complemento: Mapped[str]
    bairro: Mapped[str]
    cidade: Mapped[str]
    estado: Mapped[str]
    numero_residencia: Mapped[str]
    cliente_id: Mapped[int] = mapped_column(ForeignKey("cliente.id"))
    cliente = relationship("Cliente", back_populates="enderecos")

    def __repr__(self):
        return f"Endereco(cep={self.cep}, logradouro={self.logradouro}, complemento={self.complemento}," \
               f" bairro={self.bairro}, cidade={self.cidade}, estado={self.estado}," \
               f" numero_residencia={self.numero_residencia}, cliente_id={self.cliente_id})"
