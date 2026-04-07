class Cidade:
    def __init__(self, nome):
        self.nome = nome

class Pessoa:
    def __init__(self, nome):
        self.nome = nome 
        self.cidade = Cidade

class Animal:
    def __init__(self, nome):
        self.nome = nome 
        self.pessoa = Pessoa