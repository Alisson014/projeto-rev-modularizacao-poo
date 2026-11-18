from .livros import Livro
from .usuarios import Usuario

class Emprestimo:
    def __init__(self, livro:Livro, usuario: Usuario):
        self.livro = livro
        self.usuario = usuario
        self.ativo = True

    @property
    def livro(self):
        return self._livro

    @livro.setter
    def livro(self, livro:Livro):
        if not isinstance(livro, Livro):
            return NotImplemented
        
        if not livro.disponivel:
            raise ValueError("Livro indisponível")

        self._livro = livro

        self._livro.disponivel = False

    def devolver(self):
        self.ativo = False
        self._livro.disponivel = True

    def __str__(self):
        return f"Empréstimo:\n\t{str(self.livro)}\n\t{str(self.usuario)}\n\tAtivo: {self.ativo}"

