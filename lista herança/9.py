class Motor:
    def __init__(self, potencia):
        self.potencia = potencia
    
    def ligar_motor(self):
        print(f"Ligando motor a {self.potencia} de potencia")

class Eletrico:
    def __init__(self, bateria):
        self.bateria = bateria
    
    def carregar(self):
        print("Carregando bateria...")
    
class Combustao:
    def __init__(self, tanque):
        self.tanque = tanque
    
    def abastecer(self):
        print("Abastecendo tanque...")

class CarroEletrico(Motor, Eletrico):
    def __init__(self, potencia):
        super().__init__(potencia)
        

class CarroHibrido(Motor, Eletrico, Combustao):
    def __init__(self, potencia):
        super().__init__(potencia)

