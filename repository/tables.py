from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import type
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass
class Client(Base):
    __tablename__ = 'cliente'
    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    cpf: Mapped[str] = mapped_column(String(14), nullable=False, unique=True)
    rg: Mapped[str] = mapped_column(String(20), nullable=False)
    data_nascimento: Mapped[str] = mapped_column(type="Date", datetime=True, nullable=False)
    endereco: Mapped[List["endereco"]] = relationship(back_populates="id")

class Address(Base):
    __tablename__ = 'endereco':
    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)

