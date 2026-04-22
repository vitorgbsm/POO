class Veiculo:
    def acelerar(self):
        print("Acelerando..")
        
class Carro(Veiculo):
    def acelerar(self):
        print("Acelerando o carro..")

class Moto(Veiculo):
    def acelerar(self):
        print("Acelerando moto..")

c = Carro()
m = Moto()
c.acelerar()
m.acelerar()