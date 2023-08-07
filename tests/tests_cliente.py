import unittest
from unittest.mock import patch
from faker import Faker
from services import Cliente_service
from utils.valida_cpf import gera_cpf
from main import main


class TestStringMethods(unittest.TestCase):

    def gerar_nome_fake(self):
        fake = Faker()
        return fake.name()


    def test_cliente(self):
        nome = self.gerar_nome_fake()
        cpf = gera_cpf()
        inputs = ["1", nome, cpf, "12.345.678-x", "12/02/2001", "05003-060", "42", "0"]

        with patch("builtins.input", side_effect=inputs):
            main()


        self.assertIn(msg=f'Cliente {nome} cadastrado com sucesso!')


# Criar teste para ordens. Deve validar se a criação da ação foi bem sucedida.


