from utils.functions import formata_texto, retorna_menu
from utils.valida_cpf import valida_cpf
from utils.valida_rg import valida_rg
from utils.data import valida_data_nascimento


clientes = []

def main():
    cadastrados = []
    validador = True
    print('Seja bem vindo(a) ao sistem de gerenciamento de carteira de ações da Nuclea.\nSelecione uma das opções abaixo')



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
    nome = formata_texto()
    cpf = valida_cpf()
    rg = valida_rg()
    nascimento = valida_data_nascimento()
    cep = input('CEP:')
    numero = input('Numero da casa:')
    cliente = Cliente(nome,cpf,rg,nascimento,cep,numero)
    return cliente







def menu():
    menu = '''
    1 - Cadastrar cliente
    2 - Cadastrar ação
    3 - Realizar análise da carteira
    4 - Imprimir relatório da carteira
    5 - Sair
    Digite a opção desejada:'''

    while True:
        decision = input(menu)
        try:
            decision = int(decision)
        except ValueError as e:
            print(f'Valor{decision} inválido, tente novamente')
            continue
        except Exception as e:
            print(f'Erro desconhecido: {e}')
            continue

main()