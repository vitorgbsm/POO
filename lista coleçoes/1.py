import random

sorteio = random.sample(range(1,41), 25)
sorteio.sort()
for n in sorteio:
    print(f"{n}")