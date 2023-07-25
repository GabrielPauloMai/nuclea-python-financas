from validate_docbr import CPF

def valida_cpf(valor):
    cpf = CPF()
    while True:
        verifica = cpf.validate(valor)
        if verifica is False:
            print('Insira um valor de CPF válido!')
            valor = input('CPF:')
        else:
            return cpf.mask(valor)

