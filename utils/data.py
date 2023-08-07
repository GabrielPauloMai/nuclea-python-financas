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
            return data_convertida.date()
        else:
            print('Data de nascimento inválida!')
            continue

def valida_datas():
    datas = []
    data_atual = datetime.now().date()
    while True:
        dataincial = input('Data inicial:')
        try:
            dataincial = datetime.strptime(dataincial, '%d/%m/%Y')
            if dataincial.date() < data_atual:
                datas.append(datetime.strftime(dataincial,'%Y-%m-%d'))
                break
            else:
                print('Data inicial deve ser inferior a data atual!')
                continue
        except ValueError as e:
            print(f'{e}\n Insira uma data no formato[dd/mm/aaaa]')
            continue

    while True:
        datafinal = input('Data final:')
        try:
            datafinal = datetime.strptime(datafinal, '%d/%m/%Y')
            if datafinal.date() < dataincial.date():
                print('Data final deve ser superior a data inicial!')
            else:
                datas.append(datetime.strftime(datafinal, '%Y-%m-%d'))
                return datas
        except ValueError as e:
            print(f'{e}\n Insira uma data no formato[dd/mm/aaaa]')
            continue


if __name__ == '__main__':
    print(valida_datas())