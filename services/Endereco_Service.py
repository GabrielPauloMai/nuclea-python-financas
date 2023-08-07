from models.Endereco import Endereco
from repository.Endereco_BD import Endereco_BD
from utils.cep import busca_cep


class Endereco_Service:
    def __init__(self):
        self.endereco_bd = Endereco_BD()
        self.endereco = Endereco()

    #def cadastrar_endereco(cliente_cep, numero):
    def cadastrar_endereco(self, cliente, cliente_cep, numero):
        lista_endereco = busca_cep(cliente_cep)

        endereco = Endereco(
            cep=lista_endereco['CEP'],
            logradouro=lista_endereco['Logradouro'],
            complemento=lista_endereco['Complemento'],
            bairro=lista_endereco['Bairro'],
            cidade=lista_endereco['Cidade'],
            estado=lista_endereco['Estado'],
            numero_residencia=numero,
            cliente_id=cliente.id
        )

        self.endereco_bd.cadastrar_endereco(endereco=endereco)
        return True

    def atualizar_endereco(self, cliente, cliente_cep, numero):
        lista_endereco = busca_cep(cliente_cep)

        endereco = Endereco(
            cep=lista_endereco['CEP'],
            logradouro=lista_endereco['Logradouro'],
            complemento=lista_endereco['Complemento'],
            bairro=lista_endereco['Bairro'],
            cidade=lista_endereco['Cidade'],
            estado=lista_endereco['Estado'],
            numero_residencia=numero,
            cliente_id=cliente.id
        )

        self.endereco_bd.atualizar_endereco(endereco=endereco)
        return True

    def deletar_endereco(self, cliente):
        for endereco in cliente.enderecos:
            endereco_id = endereco.id
            resultado = self.endereco_bd.deletar_endereco(endereco_id)
            if resultado:
                return True
            else:
                return False



