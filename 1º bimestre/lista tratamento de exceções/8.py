def abrir_arquivo():
    print("Abrindo arquivo...")
    
    try:
        return 30/0
    
    except ZeroDivisionError:
        print("Erro: nao eh possivel realizar divisao por 0")
    
    finally:
        print("Fechando arquivo...")

abrir_arquivo()