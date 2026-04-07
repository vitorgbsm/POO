class Processador:
    def __init__(self, modelo, velocidade):
        self.modelo = modelo
        self.velocidade = velocidade
    
class Memoria:
    def __init__(self, capacidade):
        self.capacidade = capacidade

class Computador:
    def __init__(self):
        self.processador = Processador
        self.memoria = Memoria