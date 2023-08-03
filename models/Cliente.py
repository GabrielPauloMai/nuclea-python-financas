from utils.functions import formata_texto, retorna_menu
from utils.valida_cpf import valida_cpf
from utils.valida_rg import valida_rg
from utils.data import valida_data_nascimento
from utils.cep import valida_cep

class Cliente:
    def __init__(self):
        nome = Id
        self.cpf = None
        self.rg = None
        self.nascimento = None
        self.cep = None
        self.numero_casa = None

    def cadastrar_cliente(self):
        print('\nInforme os dados do cliente:')
        self.nome = formata_texto()
        self.cpf = valida_cpf()
        self.rg = valida_rg()
        self.nascimento = valida_data_nascimento()
        self.cep = valida_cep()
        self.numero_casa = input('Numero da casa:')
