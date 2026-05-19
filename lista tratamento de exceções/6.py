def divisao_segura(a, b):
    try:
        return a/b
    
    except ZeroDivisionError:
        print("Erro de divisao por zero")
        return None
    
    except TypeError: #acontece quando você tenta executar uma operação ou função com um tipo de dado inesperado
        print("Erro de valores: Os valores devem ser numericos")
        return None
    
print(divisao_segura(10, 8))
print(divisao_segura(12, 0))
print(divisao_segura("oi", "tudo bem?"))