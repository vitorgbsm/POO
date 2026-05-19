frase = input("Digite uma frase: ")

frase = frase.lower()

for n in ".,!?":
    frase = frase.replace(n, "")

palavras = frase.split()

unicas = set(palavras)

f = {}

for palavra in palavras:
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