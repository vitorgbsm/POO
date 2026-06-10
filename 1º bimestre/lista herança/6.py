class Nadador:
    def mover(self):
        print("Helia esta nadando e parou no meio da piscina")
    
class Corredor:
    def mover(self):
        print("Helia esta correndo")

class Triatleta(Nadador, Corredor):
    def mover(self):
        Corredor.mover(self)
        Nadador.mover(self)

t = Triatleta()
t.mover()