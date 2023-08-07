import yfinance as yf
from utils.functions import formata_titulo
class Relatorio:
    def __init__(self):
        pass

    def obter_dados_acao(self):
        try:
            acao = yf.download(self.ticker + '.SA', progress=False)

            with open(self.nome_arquivo, 'w', encoding='UTF8') as arquivo:
                arquivo.write(f"Relatorio da ação: {self.ticker} \n")
                arquivo.write(str(acao.tail()))

            print(f"Relatório exportado com sucesso para o arquivo '{self.nome_arquivo}'.")

        except Exception as e:
            print("Erro ao obter dados da ação. Verifique o código da ação e tente novamente.")
            print(f"Detalhes do erro: {e}")


    def obter_dados_usuario(self):
        path = 'relatorios/'
        self.ticker = input("Digite o código da ação na B3 (ex: PETR4): ").strip().upper()
        nome_arquivo = formata_titulo()
        self.nome_arquivo = path + nome_arquivo

    def gerar_relatorio(self):
        self.obter_dados_usuario()
        self.obter_dados_acao()
