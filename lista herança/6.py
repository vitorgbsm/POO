class Nadador:
    def mover(self):
        print("Nadando")
    
class Corredor:
    def mover(self):
        print("Correndo")

class Triatleta(Nadador, Corredor):
    def mover(self):
        Corredor.mover(self)
        Nadador.mover(self)

t = Triatleta()
t.mover()