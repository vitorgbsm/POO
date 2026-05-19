def adicionar_valor(inicial, adicional):
    if adicional <= 0:
        raise ValueError('Somente valores positivos devem ser adicionados ao valor inicial')
    
    return inicial + adicional
try:
    res = adicionar_valor(20, 16)
    print(f"O resultado da soma eh {res}")

except ValueError as a:
    print(f"Erro: {a}")

try:
    res = adicionar_valor(20,-2)
    print(F"Resultado: {res}")

except ValueError as e:
    print(f"Erro: {e}")