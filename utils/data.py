from datetime import datetime
def valida_data_nascimento():
    while True:
        data_nascimento = input('Data de nascimento: ')
        try:
            data_convertida = datetime.strptime(data_nascimento, '%d/%m/%Y')
        except ValueError as e:
            print(f'{e}\n Insira uma data no formato[dd/mm/aaaa]')
            continue

        data_atual = datetime.now().date()

        if data_convertida.date() < data_atual:
            return data_convertida.strftime('%d/%m/%Y')
        else:
            print('Data de nascimento inválida!')
            continue


if __name__ == '__main__':
    valida_data_nascimento()