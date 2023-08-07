import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Cliente
from repository.Cliente_BD import Cliente_BD

class TestClienteService(unittest.TestCase):


    def test_buscar_cliente_encontrado(self):
        self.cliente_service = Cliente_BD()
        cliente_encontrado = self.cliente_service.buscar_cliente('147.832.334-54')
        self.assertIsNotNone(cliente_encontrado)
        self.assertEqual(cliente_encontrado.nome, 'Sean Suarez')

    def test_buscar_cliente_nao_encontrado(self):
        # Testa se o cliente não é encontrado pelo CPF inexistente
        cliente_nao_encontrado = self.cliente_service.buscar_cliente('999.999.999-99')
        self.assertIsNone(cliente_nao_encontrado)
