import re


def formata_texto():
    texto = input('Nome:')
    nome_formatado = texto.title()
    return nome_formatado

def formata_titulo():
    texto = input('Dê um nome ao arquivo:')
    titulo = re.sub('.txt', '', texto)
    titulo = re.sub(r'[^\w\s]', '', titulo)
    titulo = titulo.replace(' ', '_').lower()
    titulo_formatado = texto +'.txt'
    return titulo_formatado

def valida_valor():
    while True:
        valor = input('Valor:')
        valor_formatado = valor.replace(',', '.')
        try:
            valor = float(valor_formatado)
        except ValueError:
            print('Valor inválido, tente novamente')
            continue
        except Exception as e:
            print(f'Erro desconhecido: {e}')
            continue
        if valor <= 0:
            print('Valor inválido, tente novamente')
            continue
        else:
            return valor


def valida_quantidade():
    while True:
        quantidade = input('Quantidade:')
        try:
            quantidade = int(quantidade)
        except ValueError:
            print('Quantidade inválida, tente novamente')
            continue
        except Exception as e:
            print(f'Erro desconhecido: {e}')
            continue
        if quantidade <= 0:
            print('Quantidade inválida, tente novamente')
            continue
        else:
            return quantidade

if __name__ == '__main__':

    print(valida_quantidade())
