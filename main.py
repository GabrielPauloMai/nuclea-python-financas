from services.Cliente_service import ClienteServices
from services.Acao_service import Acao_service
from services.AnaliseCarteira import AnaliseCarteira
from services.Relatorio import Relatorio
def main():
    validador = True
    print('Seja bem vindo(a) ao sistem de gerenciamento de carteira de ações da Nuclea.'
          '\nSelecione uma das opções abaixo')
    decision = ''
    while validador:
        if decision != '':
            pergunta = input('Deseja continuar neste menu? Tecle S para continuar ou qualquer outra tecla para sair')
            if pergunta.upper() == 'S':
                pass
            else:
                decision = menu()
        else:
            decision = menu()
        
        match decision:
            case 1:
                ClienteServices().menu_cliente()
            case 2:
                Acao_service().cadastar_acao()
            case 3:
                AnaliseCarteira().Show_analise()
            case 4:
                Relatorio().gerar_relatorio()
            case 5:
                print('\nObrigado por utilizar o sistema de gerenciamento de carteira de ações da Nuclea.'
                      ' \nAté a próxima!')
                break
            case default:
                print(f'Valor inválido, tente novamente')


def menu():
    menu = '\n Menu Principal:\n\t1 - Clientes\n\t2 - Cadastrar ação\n\t' \
           '3 - Realizar análise da carteira\n\t4 - Imprimir relatório da carteira' \
           '\n\t5 - Sair\n \n Digite a opção desejada:'

    while True:
        decision = input(menu)
        try:
            decision = int(decision)
            if decision >= 1 and decision <= 5:
                return decision
            else:
                print(f'Valor {decision} inválido, tente novamente')
        except ValueError as e:
            print(f'Valor {decision} inválido, tente novamente')
            continue
        except Exception as e:
            print(f'Erro desconhecido: {e}')
            continue


if __name__ == '__main__':
    main()
