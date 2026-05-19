class SenhaCurtaError(Exception):
    pass

def cadastrar_senha(senha):
    try:
        if len(senha) < 8:
            raise SenhaCurtaError("Sua senha tem menos que 8 caracteres")
        print("Senha salva com sucesso")

    except SenhaCurtaError as z:
        print(f"Erro {z}")

cadastrar_senha("1826402873")
cadastrar_senha("89267")