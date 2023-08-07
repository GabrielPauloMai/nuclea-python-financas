
CREATE TABLE cliente (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255),
    cpf VARCHAR(14) UNIQUE NOT NULL,
    rg VARCHAR(20),
    data_nascimento DATE,
    criado_em TIMESTAMP,
    atualizado_em TIMESTAMP
);


CREATE TABLE endereco (
    id SERIAL PRIMARY KEY,
    cep VARCHAR(9),
    logradouro VARCHAR(100),
    complemento VARCHAR(100),
    bairro VARCHAR(100),
    cidade VARCHAR(100) NOT NULL,
    estado VARCHAR(2) NOT NULL,
    numero_residencia VARCHAR(10),
    cliente_id INTEGER REFERENCES cliente(id)
);


CREATE TABLE acao (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    ticket VARCHAR(10),
    valor_compra FLOAT,
    quantidade_compra INTEGER,
    data_compra TIMESTAMP,
    cliente_id INTEGER REFERENCES cliente(id)
);
