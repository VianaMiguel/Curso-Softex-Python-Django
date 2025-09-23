""" Exercicio 11"""

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self):
        self.acervo = []

    def adicionar_livros(self, livro: Livro):
        self.acervo.append(livro)

    def listar_livro(self):
        for livro in self.acervo:
            print(f"O livro {livro.titulo} é do autor {livro.autor}")


livro1 = Livro("Azul", "Tim")
livro2 = Livro("Rosa", "Nino")

biblioteca = Biblioteca()
biblioteca.adicionar_livros(livro1)
biblioteca.adicionar_livros(livro2)
biblioteca.listar_livro()
