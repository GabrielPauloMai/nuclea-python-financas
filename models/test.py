from repository.Cliente_BD import Cliente_BD
from models.Cliente import Cliente
model_cliente = Cliente()
rep_cliente = Cliente_BD()

model_cliente.nome = "João"
model_cliente.cpf = "12345670510"
model_cliente.rg = "1234789"
model_cliente.data_nascimento = "1990-01-01"
# cliente.cliente.cep = "12345678"
# cliente.cliente.logradouro = "Rua 1"
# cliente.cliente.complemento = "Casa"
# cliente.cliente.bairro = "Bairro 1"
# cliente.cliente.cidade = "Cidade 1"
# cliente.cliente.estado = "SP"
# cliente.cliente.numero_residencia = "123"


rep_cliente.cadastrar_cliente(model_cliente)
rep_cliente.listar_clientes()

