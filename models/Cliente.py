from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, date
from models.Base import Base
from models.Endereco import Endereco
from models.Acao import Acao

class Cliente(Base):
    __tablename__ = 'cliente'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    nome: Mapped[str]
    cpf: Mapped[str] = mapped_column(nullable=False, unique=True)
    rg: Mapped[str]
    data_nascimento: Mapped[date]
    enderecos = relationship(Endereco, back_populates="cliente", lazy='selectin')
    acoes = relationship(Acao, back_populates="cliente",lazy='selectin')
    criado_em: Mapped[datetime]
    atualizado_em: Mapped[datetime]

    def __repr__(self):
        return f"Cliente(nome={self.nome}, cpf={self.cpf}, rg={self.rg}," \
               f" data_nascimento={self.data_nascimento}), endereço={self.enderecos}, ações={self.acoes})"
