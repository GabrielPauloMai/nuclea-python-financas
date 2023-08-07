from unittest import TestCase
from services.Acao_service import Acao_service
from unittest.mock import patch

class TestAcao_service(TestCase):

    def test_cadastar_acao(self):
        self.acao_service = Acao_service()
        inputs = ['147.832.334-54','NUSA', 'NUSA3', '10.00', '10']
        with patch("builtins.input", side_effect=inputs):
            resultado = self.acao_service.cadastar_acao()

        self.assertIn('Ação Nusa cadastrada com sucesso!', resultado)

