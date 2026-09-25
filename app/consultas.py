from sqlalchemy import select
from sqlalchemy.orm import selectinload, joinedload
from app.models import Autor, Livro
from database import ENGINE, nova_sessao

session = nova_sessao(ENGINE)

def listar_livros(session):
    statement = select(Livro)
    livros = session.scalars(statement).all()

    return livros


def livros_por_autor(session, nome_autor):
    statement = (
        select(Livro)
        .where(Livro.autor.nome.like(f"{nome_autor}"))
    )

    livros = session.scalars(statement).all()

    return livros

def buscar_livros(session, trecho):
    statement = select(Livro).where(Livro.titulo.like(f"%{trecho}%"))
    livros = session.scalars(statement).all()
    
    return livros


def listar_autores_com_quantidade(session):
    statement = select(Autor).options(selectinload(Autor.livros))
    autores = session.scalars(statement).all()

    for a in autores:
        print(f"AUTOR : {a.nome} \n LIVROS ESCRITOS: {len(a.livros)}") 
    


def detalhes_livro(session, titulo):
    statement = select(Livro).where(Livro.titulo.like(f"{titulo}")).options(joinedload(Livro.autor))
    livro = session.scalars(statement).one()

    print(f"""
        TITULO : {livro.titulo} \n
        ANO : {livro.ano} \n
        AUTOR : {livro.autor} \n
        PAIS AUTOR : {livro.autor.pais} \n
    """)