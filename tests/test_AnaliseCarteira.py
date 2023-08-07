from unittest import TestCase
from services.AnaliseCarteira import AnaliseCarteira
from unittest.mock import patch
class TestAnaliseCarteira(TestCase):
    def test_get_infos(self):
        self.fail()

    def test_cliente_nao_encontrado(self):
        self.acao_service = AnaliseCarteira()

        inputs = ['147.832.334-54']
        with patch("builtins.input", side_effect=inputs):
            resultado = self.acao_service.Show_analise()

        self.assertEqual(resultado, ['Cliente não encontrado'])

    def test_cliente_sem_acoes_cadastradas(self):
        # Simula o cenário em que o cliente não possui ações cadastradas
        resultado = self.objeto.get_infos('555.666.777-88')
        self.assertEqual(resultado, ['Cliente não possui ações cadastradas'])

    def test_cliente_com_acoes_cadastradas(self):
        # Simula o cenário em que o cliente possui ações cadastradas
        resultado = self.objeto.get_infos('147.832.334-54')
        self.assertListEqual(resultado, ['Ação1', 'Ação2', 'Ação3'])  # Substitua pelos tickets corretos

if __name__ == '__main__':
    unittest.main()

