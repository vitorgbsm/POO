class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def ligar(self):
        return f"Motor de {self.potencia} cavalos ligado."

class Carro:
    def __init__(self, modelo, motor):
        self.modelo = modelo 
        self.motor = motor 

    def ligar_carro(self):
        return f"Ligando o {self.modelo}..."

m = Motor("")
c = Carro("Toyota", m)
