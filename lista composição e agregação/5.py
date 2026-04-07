class Professor:
    def __init__(self, nome, titulaçao):
        self.nome = nome
        self.titulaçao = titulaçao

class Disciplina:
    def __init__(self, nome):
        self.nome = nome
        self.professor = Professor