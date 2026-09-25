from consultas import (
    buscar_livros,
    detalhes_livro,
    listar_autores_com_quantidade,
    listar_livros,
    livros_por_autor,
)
from database import criar_banco, nova_sessao
from seed import popular_banco


criar_banco()

with nova_sessao() as session:
    popular_banco(session)

    print("\nTodos os livros:")
    listar_livros(session)

    print("\nLivros de um autor:")
    livros_por_autor(session, "DIGITE AQUI O NOME DE UM AUTOR DO SEU SEED")

    print("\nBusca por parte do título:")
    buscar_livros(session, "DIGITE AQUI PARTE DE UM TÍTULO")

    print("\nAutores e quantidades:")
    listar_autores_com_quantidade(session)

    print("\nDetalhes de um livro:")
    detalhes_livro(session, "DIGITE AQUI O TÍTULO DE UM LIVRO DO SEU SEED")
