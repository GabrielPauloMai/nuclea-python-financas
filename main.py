from utils.functions import *
from utils.valida_cpf import *
import getpass
def main():
    cadastrados = []
    validador = True
    print('Seja bem vindo(a) ao sistem de gerenciamento de carteira de ações da Nuclea.\nSelecione uma das opções abaixo')

    menu = '''
    1 - Cadastrar cliente
    2 - Cadastrar ação
    3 - Realizar análise da carteira
    4 - Imprimir relatório da carteira
    5 - Sair
    Digite a opção desejada:'''

    while validador:
        decision = input(menu)
        try:
            decision = int(decision)
        except:
            print('Valor inválido, tente novamente')
            continue

        match decision:
            case 1:
                cliente = cadastro()
                cadastrados.append(cliente)
                for cliente in cadastrados:
                    cliente.info()
                validador = retorna_menu()
            case 5:
                break
            case default:
                print('Vamos com calma, ainda não chegamos aqui')


def cadastro():

    print('\nInforme os dados do cliente:')
    nome = formata_texto(input('Nome:'))
    cpf = valida_cpf(input(f'CPF:'))

    rg = input('RG:')
    nascimento = input('Data de Nascimento:')
    cep = input('CEP:')
    numero = input('Numero da casa:')
    cliente = Cliente(nome,cpf,rg,nascimento,cep,numero)
    return cliente




class Cliente:
    def __init__(self, nome,cpf, rg,nascimento,cep, numero):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.nascimento = nascimento
        self.cep = cep
        self.numero = numero

    def info(self):
        client_info = (f'\nNome:{self.nome}'
                f'\nCpf:{self.cpf}'
                f'\nRg:{self.rg}'
                f'\nData de nascimento:{self.nascimento} '
                f'\nCEP:{self.cep} '
                f'\nNúmero da casa:{self.numero}\n')
        print(client_info)



main()