import random

sorteio = random.sample(range(1,41), 25) #escolhendo 25 numeros entre 1 e 40 (41 nao conta)
sorteio.sort() #sort coloca a lista em ordem crescente
for n in sorteio:
    print(f"{n}")