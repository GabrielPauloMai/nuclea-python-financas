from psycopg2 import IntegrityError
from sqlalchemy.sql import select, insert, update, delete

from models.Endereco import Endereco
from repository.BancoDeDados import BancoDeDados


class Endereco_BD:

    def __init__(self):
        self.banco_de_dados = BancoDeDados()
        self.session = self.banco_de_dados.session()

    def cadastrar_endereco(self, endereco):

        insert_query = insert(endereco.__table__).values(
            cep=endereco.cep,
            logradouro=endereco.logradouro,
            complemento=endereco.complemento,
            bairro=endereco.bairro,
            cidade=endereco.cidade,
            estado=endereco.estado,
            numero_residencia=endereco.numero_residencia,
            cliente_id=endereco.cliente_id

        )

        try:
            self.session.begin()
            self.session.execute(insert_query)
            self.session.commit()
        except Exception as e:
            print('Erro ao cadastrar endereço!')
            error = e.__cause__
            if isinstance(error, IntegrityError):
                print(f'{error.pgerror}')
            self.session.rollback()
        finally:
            self.session.close()

    def listar_endereco(self):
        try:
            select_query = select(Endereco)
            result = self.session.execute(select_query)
            for row in result:
                print(row)
        except Exception as e:
            print('Erro ao listar endereços!')
            print(e)
        finally:
            self.session.close()

    def atualizar_endereco(self, endereco):
        try:
            update_query = update(Endereco).where(Endereco.id == endereco.id).values(
                cep=endereco.cep,
                logradouro=endereco.logradouro,
                complemento=endereco.complemento,
                bairro=endereco.bairro,
                cidade=endereco.cidade,
                estado=endereco.estado,
                numero_residencia=endereco.numero_residencia,
            )
            self.session.begin()
            self.session.execute(update_query)
            self.session.commit()
            print('Endereço atualizado com sucesso!')
        except Exception as e:
            print('Erro ao atualizar endereço!')
            print(e)
            self.session.rollback()
        finally:
            self.session.close()

    def deletar_endereco(self, endereco):
        try:
            delete_query = delete(Endereco).where(Endereco.id == endereco)
            self.session.begin()
            self.session.execute(delete_query)
            self.session.commit()
            print('Endereço deletado com sucesso!')
            return True
        except Exception as e:
            print('Erro ao deletar endereço!')
            print(e)
            self.session.rollback()
            return False
        finally:
            self.session.close()
