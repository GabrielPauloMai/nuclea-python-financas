import re

import requests


def busca_cep(cep):
    url = f"http://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "erro" not in data:
            endereco = {
                "CEP": data['cep'],
                "Logradouro": data['logradouro'],
                "Complemento": data['complemento'],
                "Bairro": data['bairro'],
                "Cidade": data['localidade'],
                "Estado": data['uf']
            }

            return endereco


def valida_cep():
    while True:
        cep_input = re.sub('-', '', input("CEP: "))

        if cep_input.isdigit() and len(cep_input) == 8:
            retorno_cep = busca_cep(cep_input)
            if retorno_cep:
                return cep_input
            else:
                print("CEP não encontrado ou inválido.")
        else:
            print("Digite um CEP válido. Ex: 00000-000 ou 00000000")


if __name__ == "__main__":
    valida_cep()
