with open ("lista serialização de objetos/convidados.txt", "a") as b:
    for i in range(5):
        n = input("Digite seu nome:")
        b.write(f"{n}\n")