frase = input("Digite uma frase: ")

frase = frase.lower() #tudo minusculo

for n in ".,!?":
    frase = frase.replace(n, "") #remove pontuaçao e coloca nada ao inves disso

palavras = frase.split() #separa em partes

unicas = set(palavras) #separa em conjuntos sem repetições

f = {}

for palavra in palavras: #soma as palavras repetidas
    if palavra in f:
        f[palavra] += 1
    else:
        f[palavra] = 1

print("Palavras unicas: ")
for palavra in sorted(unicas):
    print(palavra)

print("Frequencia das palavras:")
for palavra in sorted(f):
    print(f"{palavra}: {f[palavra]}")