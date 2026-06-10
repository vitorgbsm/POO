from abc import ABC, abstractmethod

class DispositivoEletronico(ABC):
    @abstractmethod
    def ligar(self):
        return 'ligando'
    
    @abstractmethod
    def desligar(self):
        return 'desligando'
    
class Carregavel(ABC):
    @abstractmethod
    def carregar(self):
        return 'Carregando'


# --------------------------------------

class Smartphone(DispositivoEletronico, Carregavel):
    def ligar(self):
        return 'Ligando Smartphone'

    def desligar(self):
        return 'Desligando Smartphone'
    
    def carregar(self):
        return 'Carregando Smartphone'


class Notebook(DispositivoEletronico, Carregavel):
    def ligar(self):
        return 'Ligando Notebook'

    def desligar(self):
        return 'Desligando Notebook'
    
    def carregar(self):
        return 'Carregando Notebook'


class FoneDeOuvido(DispositivoEletronico):
    def ligar(self):
        return 'Fone de ouvido Ligando'
    
    def desligar(self):
        return 'Fone de ouvido Desligando'
    

# --------------------------------------


dispositivos_eletronicos = [Smartphone(), Notebook(), FoneDeOuvido()]
dispositivos_carregaveis = [Smartphone(), Notebook()]

for dispositivo in dispositivos_eletronicos:
    print(f'{dispositivo.ligar()}')
    print(f'{dispositivo.desligar()} \n')

for dispositivo in dispositivos_carregaveis:
    print(f'{dispositivo.carregar()}')