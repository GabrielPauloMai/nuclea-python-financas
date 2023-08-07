import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from utils.data import valida_datas
from utils.valida_cpf import valida_cpf
from services.Cliente_service import ClienteServices

class AnaliseCarteira:

    def __init__(self):
        self.cliente = ClienteServices()
        self.lista = []
        self.datas = []

    def get_infos(self):
        print('Informe o cliente desejado')
        cpf = valida_cpf()
        self.cliente = self.cliente.verifica_cpf(cpf=cpf)
        if not self.cliente:
            return (f'Cliente não encontrado')
        for acao in self.cliente.acoes:
            self.lista.append(f'{acao.ticket}.SA')
        if len(self.lista) == 0:
            print ('Cliente não possui ações cadastradas')
            return False
        print('Informe o período de data desejado')
        self.datas = valida_datas()

    def get_cotacoes(self):
        df = pd.DataFrame()

        for i in self.lista:
            cotacao = yf.download(i, start=self.datas[0], end=self.datas[1])
            df[i] = cotacao['Adj Close']

        df.plot(figsize=(15, 10))
        plt.xlabel('Anos')
        plt.ylabel('Valor Ticket')
        plt.title(f'Variação de valor das ações da carteira do cliente {self.cliente.nome}')
        plt.legend()
        plt.show()
        return True


    def Show_analise(self):
        resultado = self.get_infos()
        if resultado:
            self.get_cotacoes()
            return True
        else:
            return False