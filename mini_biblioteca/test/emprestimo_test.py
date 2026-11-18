
from src.mini_biblioteca import Emprestimo, Livro, Usuario
import pytest

# Criando usuário
usuario = Usuario("José Alisson", 1)

# Criando livro
livro = Livro("The Hobbit", "J.R.R Tolkien", "014")

# Criando empréstimo
empr = Emprestimo(livro, usuario)


def test_nao_cria_indisponivel():
    livro.disponivel = False
    with pytest.raises(ValueError):
        Emprestimo(livro, usuario)
