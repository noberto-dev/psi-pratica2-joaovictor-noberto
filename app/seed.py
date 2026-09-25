from models import Autor, Livro
from database import nova_sessao, create_engine, ENGINE


session = nova_sessao(ENGINE)

def popular_banco(session):
    user1 = Autor("P.H. Medeiros","Japão")
    user2 = Autor("Jeizon Gomes da Silva Filho","Estados Unidos")

    livros = [
        Livro(nome="Vendedor de Sonhos", ano=2026, autor=user1),
        Livro(nome="Primeira Análise de Jesus Cristo", ano=-2000, autor=user1),
        Livro(nome="Tsunami: A Revanche", ano=2020, autor=user1),
        Livro(nome="GPT 5: Como se tornar o Mestre da IA", ano=2028, autor_id=user2.id, autor=user2),
        Livro(nome="IA: O Domínio", ano=2030, autor=user2, autor_id=user2.id),
        Livro(nome="Do lixo ao domínio: Inteligencias Artificiais", ano=2027, autor_id=user2.id, autor=user2)
    ]
    for l in livros:
        session.add(l)

    session.add_all([user1, user2])
    session.commit()

if __name__ ==  "__main__":
    popular_banco()



    
