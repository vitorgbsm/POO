class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def exibir_detalhes(self):
        print(f"tiutlo: {self.titulo} - autor: {self.autor}, {self.isbn}")

class Membro:
    def __init__(self, nome, id_membro, contato):
        self.nome = nome
        self.id_membro = id_membro
        self.contato = contato

l = Livro("borboletinha na cozinha", "Galinha pintadinha", 123124421)
l.exibir_detalhes()