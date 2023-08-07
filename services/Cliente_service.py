from models.Cliente import Cliente
from repository.Cliente_BD import Cliente_BD
from utils.data import valida_data_nascimento
from utils.functions import formata_texto
from utils.valida_cpf import valida_cpf
from utils.valida_rg import valida_rg
from utils.cep import valida_cep
from services.Endereco_Service import Endereco_Service
from datetime import date


class ClienteServices:
    def __init__(self):
        self.cliente_bd = Cliente_BD()
        self.cliente = Cliente
        self.endereco_service = Endereco_Service()

    def cadastrar_cliente(self):
        print('\nInforme os dados do cliente:')
        nome = formata_texto()
        cpf = valida_cpf()
        rg = valida_rg()
        nascimento = valida_data_nascimento()
        cep = valida_cep()
        numero = input('Numero da casa:')

        cliente = Cliente(
            nome=nome,
            cpf=cpf,
            rg=rg,
            data_nascimento=nascimento,
        )

        if not self.cliente_bd.verifica_cpf(cpf):
            print(f'Já existe cliente com o cpf {cpf} cadastrado, tente novamente com'
                    f' outro cpf ou atualize o existente!')
            return(f'Já existe cliente com o cpf {cpf} cadastrado, tente novamente com'
                  f' outro cpf ou atualize o existente!')
        else:
            pass

        self.cliente.id = self.cliente_bd.cadastrar_cliente(cliente)
        self.endereco_service.cadastrar_endereco(cliente, cliente_cep=cep, numero=numero)
        print(f'\nCliente {cliente.nome} cadastrado com sucesso!\n')
        return (f'\nCliente {cliente.nome} cadastrado com sucesso!\n')
    def verifica_cpf(self, cpf):

        return self.cliente_bd.buscar_cliente(cpf)
    def cliente_informacoes(self):
        print('\nInforme o cpf do cliente:')
        cpf = valida_cpf()

        cliente = self.cliente_bd.buscar_cliente(cpf)
        if cliente:
            print(f'\nInformações do cliente:\n')
            print(f'Cliente: {cliente.nome}\nCPF: {cliente.cpf}\nRG: {cliente.rg}\nData de nascimento: '
                  f'{cliente.data_nascimento}\n')
            for endereco in cliente.enderecos:
                print(f'Endereço:\nCEP: {endereco.cep}\nLogradouro: {endereco.logradouro}\n Complemento:{endereco.complemento}'
                      f'\nBairro: {endereco.bairro}\nCidade: {endereco.cidade}\nEstado: {endereco.estado}\n'
                      f'Número da casa: {endereco.numero_residencia}\n')
                return (f'Informações do cliente: {cliente.nome}\nCPF: {cliente.cpf}')
        else:
            print(f'Não existe cliente com o cpf {cpf} cadastrado!')

    def listar_clientes(self):
        lista_clientes = self.cliente_bd.listar_clientes()
        if lista_clientes:
            print(f'\nLista de clientes:\n')
            print(f'| {"ID":<4} | {"Nome":<20} | {"CPF":<14} | {"RG":<12} | {"Nascimento":<10} |')
            for cliente in lista_clientes:
                cliente = cliente._data[0]
                print(f'| {cliente.id:4} | {cliente.nome:<20} | {cliente.cpf:<14} | {cliente.rg:<12} | {cliente.data_nascimento.strftime("%d/%m/%Y"):<10} |')
            return (f'Clientes listados com sucesso!')
        else:
            return('Não existem clientes cadastrados!')


    def alterar_cliente(self):
        print('\nInforme o cpf do cliente:')
        cpf = valida_cpf()

        cliente = self.cliente_bd.buscar_cliente(cpf)
        if cliente:
            print(f'\nInforme os novos dados do cliente:')
            print(f'Nome atual: {cliente.nome}')
            nome = formata_texto()
            print(f'RG atual: {cliente.rg}')
            rg = valida_rg()
            print(f'Data de nascimento atual: {cliente.data_nascimento.strftime("%d/%m/%Y")}')
            nascimento = valida_data_nascimento()
            print(f'Endereço atual: {cliente.enderecos}')
            cep = valida_cep()
            numero = input('Número da casa:')

            cliente.nome = nome
            cliente.rg = rg
            cliente.data_nascimento = nascimento

            self.endereco_service.atualizar_endereco(cliente, cliente_cep=cep, numero=numero)

            self.cliente_bd.atualizar_cliente(cliente)
            print(f'\nCliente {cliente.nome} atualizado com sucesso!\n')
            return (f'Cliente {cliente.nome} atualizado com sucesso!')
        else:
            print(f'Não existe cliente com o cpf {cpf} cadastrado!')

    def deletar_cliente(self):
        print('\nInforme o cpf do cliente:')
        cpf = valida_cpf()

        cliente = self.cliente_bd.buscar_cliente(cpf)
        if cliente:

            while True:
                print(f'\nDeseja realmente deletar o cliente {cliente.nome}?')
                decision = input('1 - Sim\n2 - Não\n')
                try:
                    decision = int(decision)
                except Exception as e:
                    print(f'Valor inválido, tente novamente\n {e}')
                    continue
                if decision == 1 or decision == 2:
                    break
                else:
                    print(f'Valor inválido, tente novamente')
                    continue

            if decision == 1:
                resultado = self.endereco_service.deletar_endereco(cliente)
                if resultado:
                    resultado = self.cliente_bd.deletar_cliente(cliente)
                    if resultado:
                        print(f'\nCliente {cliente.nome} deletado com sucesso!\n')
                        return (f'\nCliente {cliente.nome} deletado com sucesso!\n')
                    else:
                        print(f'Erro ao deletar cliente!')
                        return (f'Erro ao deletar cliente!')
                else:
                    print(f'Erro ao deletar cliente!')
                    return (f'Erro ao deletar cliente!')
            else:
                print(f'\nOperação cancelada!\n')
        else:
            print(f'Não existe cliente com o cpf {cpf} cadastrado!')

    def voltar_menu(self,decision):
        while True:
            match decision:
                case 1:
                    self.cadastrar_cliente()
                case 2:
                    self.cliente_informacoes()
                case 3:
                    self.listar_clientes()
                case 4:
                    self.alterar_cliente()
                case 5:
                    self.deletar_cliente()
                case 0:
                    break
                case default:
                    print(f'Valor inválido, tente novamente')
                    break
            voltar = input('\nDeseja continuar neste submenu?\n(Tecle S para continuar ou qualquer '
                           'outra tecla para voltar ao menu principal):')
            if voltar.upper() == 'S':
                continue
            else:
                break
    def menu_cliente(self):
        opcoes = '\n Menu do cliente:\n\t1 - Cadastrar um cliente\n\t2 - Visualizar um cliente\n\t' \
                 '3 - Listar todos os clientes\n\t4 - Alterar um cliente\n\t5 - Deletar um usuário\n \t0 - Voltar\n Opção:'
        while True:
            decision = input(opcoes)
            try:
                decision = int(decision)
            except Exception as e:
                print(f'Valor inválido, tente novamente\n {e}')
                continue
            if decision == 0:
                break
            elif decision >= 1 and decision <= 5:
                self.voltar_menu(decision)
            else:
                print(f'Valor inválido, tente novamente')
                continue





