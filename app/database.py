from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session


# TODO: crie a classe Base herdando de DeclarativeBase.
class Base(DeclarativeBase):
    def __init__(self):
        super().__init__()

# TODO: crie a engine apontando para sqlite:///biblioteca.db.

ENGINE = create_engine("sqlite:///biblioteca.db")

def criar_banco():
    Base.metadata.create_all(bind=ENGINE)
    return

def nova_sessao(engine):
    session = Session(engine)
    return session

