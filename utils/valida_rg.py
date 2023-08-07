import re


def valida_rg():

    pattern = r"^\d{2}.\d{3}.\d{3}-[A-Z a-z 0-9]$"
    while True:
        rg = input('RG:')
        if re.match(pattern, rg):
            return rg
        else:
            print('RG inválido!')
            continue

if __name__ == '__main__':
    valida_rg()