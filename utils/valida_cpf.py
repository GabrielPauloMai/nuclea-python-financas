from validate_docbr import CPF

def valida_cpf():
    cpf = CPF()
    while True:
        valor = input('CPF:')
        verifica = cpf.validate(valor)
        if verifica is False:
            print('Insira um valor de CPF válido!')
            valor = input('CPF:')
        else:
            return cpf.mask(valor)

if __name__ == '__main__':
    valida_cpf()