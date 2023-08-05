from sqlalchemy import create_engine
from sqlalchemy import URL
from sqlalchemy.orm import sessionmaker


class BancoDeDados:

    def __init__(self):
        self.engine = create_engine(self.url_conexao)

    def __del__(self):
        self.session().close()
        self.engine.dispose()

    url_conexao = URL.create(
        "postgresql",
        username="postgres",
        password="root",
        host="localhost",
        port=5432,
        database="nuclea",
    )

    def session(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session
