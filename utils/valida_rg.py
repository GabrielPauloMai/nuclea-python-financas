import re


def valida_rg(rg):
    pattern = r"^\d{2}.\d{3}.\d{3}-[A-Z 0-9]$"
    while True:
        if re.match(pattern, rg):
            return rg
        else:
            print('RG inválido!')
            rg = input('RG:')
            continue
