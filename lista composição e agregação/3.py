class Autor:
    def __init__(self, autor):
        self.autor = autor

class Livro:
    def __init__(self, livro):
        self.livro = livro
        self.autor = Autor