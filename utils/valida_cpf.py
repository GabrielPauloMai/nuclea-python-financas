from validate_docbr import CPF
import re
def valida_cpf():
    cpf = CPF()
    while True:
        valor = re.sub('[.-]','',input(f'CPF: '))
        verifica = cpf.validate(valor)
        if verifica is False:
            print('Insira um valor de CPF válido!')
        else:
            return cpf.mask(valor)

def gera_cpf():
    cpf = CPF()
    return cpf.generate()

if __name__ == '__main__':
    valida_cpf()