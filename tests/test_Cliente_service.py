from unittest import TestCase
from unittest.mock import patch
from faker import Faker
from utils.valida_cpf import gera_cpf, formata_cpf
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
            resultado = serv.cadastrar_cliente()

        self.assertTrue(f'Cliente {nome} cadastrado com sucesso!',resultado)

    def test_cliente_informacoes(self):
        from services.Cliente_service import ClienteServices
        nome = self.gerar_nome_fake()
        cpf = gera_cpf()
        serv = ClienteServices()

        inputs = [nome, cpf, "12.345.678-x", "12/02/2001", "05003-060", "42"]
        with patch("builtins.input", side_effect=inputs):
            serv.cadastrar_cliente()

        inputs = [cpf]

        with patch("builtins.input", side_effect=inputs):
            resultado = serv.cliente_informacoes()

        self.assertIn(f'Informações do cliente: {nome}\nCPF: {formata_cpf(cpf)}', resultado)

    def test_listar_clientes(self):
        serv = ClienteServices()
        resultado = serv.listar_clientes()
        self.assertIn('Clientes listados com sucesso!',resultado)

    def test_alterar_cliente(self):

        from services.Cliente_service import ClienteServices
        nome = self.gerar_nome_fake()
        cpf = gera_cpf()
        serv = ClienteServices()

        inputs = [nome, cpf, "12.345.678-x", "12/02/2001", "05003-060", "42"]
        with patch("builtins.input", side_effect=inputs):
            serv.cadastrar_cliente()

        inputs = [cpf, 'Gabriel Paulo Mai', '10.003.019-x', '10/09/2000', '89278-000', '319']
        with patch("builtins.input", side_effect=inputs):
            resultado = serv.alterar_cliente()
        self.assertIn('Cliente Gabriel Paulo Mai atualizado com sucesso!',resultado)


    def test_deletar_cliente(self):
        from services.Cliente_service import ClienteServices
        nome = self.gerar_nome_fake()
        cpf = gera_cpf()
        serv = ClienteServices()

        inputs = [nome, cpf, "12.345.678-x", "12/02/2001", "05003-060", "42"]
        with patch("builtins.input", side_effect=inputs):
            serv.cadastrar_cliente()

        inputs = [cpf, '1']
        with patch("builtins.input", side_effect=inputs):
            resultado = serv.deletar_cliente()
        self.assertIn(f'\nCliente {nome} deletado com sucesso!\n', resultado)

    def test_verifica_cpf(self):
        self.fail()


