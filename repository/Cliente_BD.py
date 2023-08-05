from datetime import datetime

from psycopg2 import IntegrityError
from sqlalchemy.sql import select, insert, update, delete

from models.Cliente import Cliente
from repository.BancoDeDados import BancoDeDados


class Cliente_BD:

    def __init__(self):
        self.banco_de_dados = BancoDeDados()
        self.session = self.banco_de_dados.session()

    def cadastrar_cliente(self, cliente):

        insert_query = insert(cliente.__table__).values(
            nome=cliente.nome,
            cpf=cliente.cpf,
            rg=cliente.rg,
            data_nascimento=cliente.data_nascimento,
            criado_em=datetime.now(),
            atualizado_em=datetime.now()
        )

        try:
            self.session.begin()
            self.session.execute(insert_query)
            self.session.commit()
            print('Usuário cadastrado com sucesso!')
        except Exception as e:
            print('Erro ao cadastrar usuário!')
            error = e.__cause__
            if isinstance(error, IntegrityError):
                print(f'{error.pgerror}')
            self.session.rollback()
        finally:
            self.session.close()

    def listar_clientes(self):
        try:
            select_query = select(Cliente)
            result = self.session.execute(select_query)
            for row in result:
                print(row)
        except Exception as e:
            print('Erro ao listar clientes!')
            print(e)
        finally:
            self.session.close()

    def atualizar_cliente(self, cliente):
        try:
            update_query = update(Cliente).where(Cliente.id == cliente.id).values(
                nome=cliente.nome,
                cpf=cliente.cpf,
                rg=cliente.rg,
                data_nascimento=cliente.data_nascimento,
                atualizado_em=datetime.now()
            )
            self.session.begin()
            self.session.execute(update_query)
            self.session.commit()
            print('Cliente atualizado com sucesso!')
        except Exception as e:
            print('Erro ao atualizar cliente!')
            e = e.__cause__
            print(e.pgerror)
            self.session.rollback()
        finally:
            self.session.close()

    def deletar_cliente(self, cliente):
        delete_query = delete(Cliente).where(Cliente.id == cliente.id)
        try:
            self.session.begin()
            self.session.execute(delete_query)
            self.session.commit()
            print('Cliente deletado com sucesso!')
        except Exception as e:
            print('Erro ao deletar cliente!')
            print(e)
            self.session.rollback()
        finally:
            self.session.close()
