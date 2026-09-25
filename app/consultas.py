from sqlalchemy import select
from sqlalchemy.orm import selectinload, joinedload
from models import Autor, Livro
from database import ENGINE, nova_sessao

session = nova_sessao(ENGINE)

def listar_livros(session):
    statement = select(Livro).options(joinedload(Livro.autor))
    livros = session.scalars(statement).all()

    for l in livros:
            print(f"""
                TITULO : {l.titulo} \n
                ANO : {l.ano} \n
                AUTOR : {l.autor.nome} \n
            """)
    


def livros_por_autor(session, nome_autor):
    statement = (
        select(Livro)
        .where(Livro.autor.has(Autor.nome.like(f"{nome_autor}")))
    )

    livros = session.scalars(statement).all()

    for l in livros:
            print(f"""
                TITULO : {l.titulo} \n
                ANO : {l.ano} \n
                AUTOR : {l.autor.nome} \n
            """)
    


def buscar_livros(session, trecho):
    statement = select(Livro).where(Livro.titulo.like(f"%{trecho}%"))
    livros = session.scalars(statement).all()
    
    for l in livros:
        print(f"""
            TITULO : {l.titulo} \n
            ANO : {l.ano} \n
            AUTOR : {l.autor.nome} \n
        """)

def listar_autores_com_quantidade(session):
    statement = select(Autor).options(selectinload(Autor.livros))
    autores = session.scalars(statement).all()

    for a in autores:
        print(f"AUTOR : {a.nome} \n LIVROS ESCRITOS: {len(a.livros)}") 
    


def detalhes_livro(session, titulo):
    statement = select(Livro).where(Livro.titulo.like(f"{titulo}")).options(joinedload(Livro.autor))
    livro = session.scalars(statement).first()

    print(f"""
        TITULO : {livro.titulo} \n
        ANO : {livro.ano} \n
        AUTOR : {livro.autor} \n
        PAIS AUTOR : {livro.autor.pais} \n
    """)