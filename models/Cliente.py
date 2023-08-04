from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, date
from typing import List
from models.Base import Base
class Cliente(Base):
    __tablename__ = 'cliente'
    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True, index=True)
    nome: Mapped[str] = mapped_column(length=100, nullable=False)
    cpf: Mapped[str] = mapped_column(length=14, nullable=False, unique=True)
    rg: Mapped[str] = mapped_column(length=20)
    data_nascimento: Mapped[date]
    endereco: Mapped[List["endereco"]] = relationship(back_populates="cliente_id")
    criado_em: Mapped[datetime]
    atualizado_em: Mapped[datetime]

    def __repr__(self):
        return f"Cliente(nome={self.nome}, cpf={self.cpf}, rg={self.rg}," \
               f" data_nascimento={self.data_nascimento}," \
               f" endereco={self.endereco}, criado_em={self.criado_em}, atualizado_em={self.atualizado_em})"
