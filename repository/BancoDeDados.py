from sqlalchemy import create_engine
from sqlalchemy import URL


class BancoDeDados:

    def __init__(self):
        self.engine = create_engine(self.url_conexao)
        self.cursor = self.engine.connect()

    def __del__(self):
        self.cursor.close()
        self.engine.dispose()

    url_conexao = URL.create(
        "postgresql",
        username="postgres",
        password="root",
        host="0.0.0.0",
        port=5432,
        database="nuclea",
    )
