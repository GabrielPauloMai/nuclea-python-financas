import datetime
from typing import List
from sqlalchemy import Integer, String, Float, Date, DateTime, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    type_annotations_map = {
        int: Integer,
        datetime.datetime: DateTime,
        datetime.date: Date,
        bool: Boolean,
        float: Float(10,2),
    }
class Cliente(Base):
    __tablename__ = 'cliente'
    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    cpf: Mapped[str] = mapped_column(String(14), nullable=False, unique=True)
    rg: Mapped[str] = mapped_column(String(20), nullable=False)
    data_nascimento: Mapped[datetime.date] = mapped_column( datetime=True, nullable=False)
    endereco: Mapped[List["endereco"]] = relationship(back_populates="cliente_id")
    criado_em: Mapped[datetime.datetime] = mapped_column( datetime=True, nullable=False)
    atualizado_em: Mapped[datetime.datetime] = mapped_column(datetime=True, nullable=False)

    def __repr__(self):
        return f"Cliente(nome={self.nome}, cpf={self.cpf}, rg={self.rg}, data_nascimento={self.data_nascimento}, endereco={self.endereco}, criado_em={self.criado_em}, atualizado_em={self.atualizado_em})"

class Address(Base):
    __tablename__ = 'endereco'
    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    cep: Mapped[str] = mapped_column(String(9), nullable=False)
    logradouro: Mapped[str] = mapped_column(String(100), nullable=True)
    complemento: Mapped[str] = mapped_column(String(100), nullable=True)
    bairro: Mapped[str] = mapped_column(String(100), nullable=True)
    cidade: Mapped[str] = mapped_column(String(100), nullable=False)
    estado: Mapped[str] = mapped_column(String(2), nullable=False)
    numero_residencia: Mapped[str] = mapped_column(String(10), nullable=True)
    cliente_id: Mapped[int] = mapped_column(ForeignKey("cliente.id"), nullable=False)

    def __repr__(self):
        return f"Endereco(cep={self.cep}, logradouro={self.logradouro}, complemento={self.complemento}, bairro={self.bairro}, cidade={self.cidade}, estado={self.estado}, numero_residencia={self.numero_residencia}, cliente_id={self.cliente_id})"

class Acao(Base):
    __tablename__ = 'acao'
    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    ticket: Mapped[str] = mapped_column(String(10), nullable=False)
    valor_compra: Mapped[float] = mapped_column(type="Float", nullable=False)
    quantidade_compra: Mapped[int] = mapped_column(type="Integer", nullable=False)
    data_compra: Mapped[str] = mapped_column(type="Date", datetime=True, nullable=False)
    cliente_id: Mapped[int] = mapped_column(ForeignKey("cliente.id"), nullable=False)

    def __repr__(self):
        return f"Acao(nome={self.nome}, ticket={self.ticket}, valor_compra={self.valor_compra}, quantidade_compra={self.quantidade_compra}, data_compra={self.data_compra}, cliente_id={self.cliente_id})"

