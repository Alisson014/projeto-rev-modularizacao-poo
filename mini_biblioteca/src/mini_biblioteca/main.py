from .__init__ import Livro, Usuario, Emprestimo

print("Criando classes: ")
# Criando usuário
usuario = Usuario("José Alisson", 1)
print(usuario)

# Criando livro
livro = Livro("The Hobbit", "J.R.R Tolkien", "014")
print(livro)

# Criando empréstimo
empr = Emprestimo(livro, usuario)
print(empr)

print()
print("Devolvendo:")
# Devolvendo
empr.devolver()

print(empr)
