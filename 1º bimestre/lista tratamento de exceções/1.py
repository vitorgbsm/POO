def adicionar_valor(inicial, adicional):
    if adicional <= 0:
        raise ValueError('Somente valores positivos devem ser adicionados ao valor inicial') #se for menor ou igual a zero, gera um erro de valor
    
    return inicial + adicional #se nao der erro, a funçao soma normal
try:
    res = adicionar_valor(20, 16)
    print(f"O resultado da soma eh {res}") 

except ValueError as a:
    print(f"Erro: {a}") #o except ocorre quando o try anterior dá erro, aí gera esse print, caso não dê, nao gera

try:
    res = adicionar_valor(20,-2)
    print(F"Resultado: {res}")

except ValueError as e:
    print(f"Erro: {e}")