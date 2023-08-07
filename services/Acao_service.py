from models.Acao import Acao
from utils.functions import formata_texto, valida_valor, valida_quantidade
from utils.valida_cpf import valida_cpf
from services.Cliente_service import ClienteServices
from repository.Acao_BD import Acao_BD

class Acao_service:
    def __init__(self):
        self.acao = Acao()
        self.cliente = ClienteServices()
        self.acao_banco = Acao_BD()

    def cadastar_acao(self):
        print('Cadastro de ação')
        print('Informe o comprador')
        cpf = valida_cpf()

        cliente_id = self.cliente.verifica_cpf(cpf)
        if not cliente_id:
            print(f'Comprador não encontrado')
            return False
        nome = formata_texto()
        ticket = input('Digite o ticket da ação: ')
        valor = valida_valor()
        quantidade = valida_quantidade()
        acao = Acao(
            nome=nome,
            ticket=ticket,
            valor_compra=valor,
            quantidade_compra=quantidade,
            cliente_id=cliente_id.id
        )

        self.acao_banco.cadastrar_acao(acao)
        return(f'\nAção {nome} cadastrada com sucesso!')

    def deletar_acao(self, cliente):
        for acao in cliente.acoes:
            acao_id = acao.id
            self.acao_banco.deletar_acao(acao_id)
        return(f'\nAções do cliente deletadas com sucesso!')
