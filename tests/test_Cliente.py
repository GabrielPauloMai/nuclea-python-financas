from unittest import TestCase
from unittest.mock import patch
from models.Cliente import Cliente

class TestCliente(TestCase):
    cliente = Cliente()
    cliente = ['Gabriel Paulo Mai', '10.003.019-x', '10/09/2000', '89278-000', '319']
    Cliente.__repr__(cliente)
