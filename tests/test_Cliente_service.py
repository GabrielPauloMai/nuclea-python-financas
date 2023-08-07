from unittest import TestCase
from unittest.mock import patch
from faker import Faker
from utils.valida_cpf import gera_cpf
from services.Cliente_service import ClienteServices


class TestClienteServices(TestCase):

    def gerar_nome_fake(self):
        fake = Faker()
        return fake.name()

    def test_cadastra_cliente(self):
        serv = ClienteServices()
        nome = self.gerar_nome_fake()
        cpf = gera_cpf()
        inputs = [nome, cpf, "12.345.678-x", "12/02/2001", "05003-060", "42"]

        with patch("builtins.input", side_effect=inputs):
            serv.cadastrar_cliente()

        self.assertTrue(expr="", msg=f'Cliente {nome} cadastrado com sucesso!')

    def test_cliente_informacoes(self):
        from services.Cliente_service import ClienteServices

        serv = ClienteServices()
        cpf = '147.832.334-54'
        inputs = [cpf]

        with patch("builtins.input", side_effect=inputs):
            serv.cliente_informacoes()

        self.assertIn(cliente_esperado, cliente_esperado)

        self.fail()

    def test_listar_clientes(self):
        serv = ClienteServices()
        teste = serv.listar_clientes()
        self.assertTrue(msg='Lista de clientes:')
        self.fail(msg='Não foi possível listar os clientes!')

    def test_alterar_cliente(self):
        from services.Cliente_service import ClienteServices
        serv = ClienteServices()
        inputs = ['26649254746', 'Gabriel Paulo Mai', '10.003.019-x', '10/09/2000', '89278-000', '319']
        with patch("builtins.input", side_effect=inputs):
            serv.alterar_cliente()

        self.fail()

    def test_deletar_cliente(self):
        from services.Cliente_service import ClienteServices
        serv = ClienteServices()
        inputs = ['43287944185', '1']
        with patch("builtins.input", side_effect=inputs):
            serv.deletar_cliente()


    def test_verifica_cpf(self):
        self.fail()
