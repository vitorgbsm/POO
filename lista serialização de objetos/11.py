def registrar_log(mensagem):
    with open ("lista serialização de objetos/sistema.log", "a") as s:
        s.write(f"{mensagem}\n")

registrar_log("oi tudo bem")
registrar_log("oi tudo bem")
registrar_log("oi tudo bem")