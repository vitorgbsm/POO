from abc import ABC, abstractmethod

class Controlavel(ABC):
    @abstractmethod
    def mover(self):
        pass

class Jogador(Controlavel):
    def mover(self):
        return 'Jogador se movendo'

class Volante(Controlavel):
    def mover(self):
        return 'Volante girando'

move = [Jogador(), Volante()]
for m in move:
    print(m.mover())