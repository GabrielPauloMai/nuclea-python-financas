def retorna_menu():
    decision = input('Deseja retornar ao menu principal?(S/N)')
    if decision.upper() == 'N':
        return False
    else:
        return True


def formata_texto():
    texto = input('Nome:')
    nome_formatado = texto.title()
    return nome_formatado

