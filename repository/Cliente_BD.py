import BancoDeDados
from models.Cliente import Cliente
from sqlalchemy.sql import select, insert, update, delete


class Cliente_DB:

    def __init__(self):
        self.banco_de_dados = BancoDeDados()
        cliente = Cliente()

    def cadastrar_cliente(self):
        select().Cliente().all()
        self.cpf = "cpf"
        self.banco_de_dados.insert()
    def consultar_cliente(self):
        clientes = self.banco_de_dados.session.query(Cliente).all()

        for cliente in clientes:
            print(cliente.nome, cliente.email)
        pass

    def alterar_cliente(self):
        pass

    def delete_cliente(self):
        pass