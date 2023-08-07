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
        # cpf = valida_cpf()
        cpf = '147.832.334-54'
        self.cliente = self.cliente.verifica_cpf(cpf=cpf)
        if not self.cliente:
            return (f'Cliente não encontrado')
        for acao in self.cliente.acoes:
            self.lista.append(f'{acao.ticket}.SA')
        print('Informe o período de data desejado')
        #self.datas = valida_datas()
        self.datas = ['2020-01-01', '2023-01-01']

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
        self.get_infos()
        self.get_cotacoes()
        return True