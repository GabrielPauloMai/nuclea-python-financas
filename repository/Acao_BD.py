from models.Acao import Acao
from datetime import datetime

from sqlalchemy.sql import select, insert, delete
from repository.BancoDeDados import BancoDeDados

class Acao_BD:
    def __init__(self):
        self.banco_de_dados = BancoDeDados()
        self.session = self.banco_de_dados.session()

    def cadastrar_acao(self, acao):
        insert_query = insert(acao.__table__).values(
            nome=acao.nome,
            ticket=acao.ticket,
            valor_compra=acao.valor_compra,
            quantidade_compra=acao.quantidade_compra,
            data_compra=datetime.now(),
            cliente_id=acao.cliente_id
        )
        try:
            self.session.begin()
            self.session.execute(insert_query)
            self.session.commit()
        except Exception as e:
            print(f'Erro ao cadastrar ação!\n Erro: {e} ')
            self.session.rollback()
        finally:
            self.session.close()

    def deletar_acao(self, acao_id):
        delete_query = delete(Acao).where(Acao.id == acao_id)
        try:
            self.session.begin()
            self.session.execute(delete_query)
            self.session.commit()
        except Exception as e:
            print('Erro ao deletar ação!')
            print(e)
            self.session.rollback()
        finally:
            self.session.close()