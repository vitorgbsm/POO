contagem = {}
while True:
    e = input(int("Digite o ano de nascmento"))

    if e == "":
        break

    else:
        ano = int(e)
        if ano in contagem:
            contagem[ano] += 1

        else:
            contagem[ano] = 1