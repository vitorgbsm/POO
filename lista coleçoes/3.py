agenda = {}

def adicionar_contato (agenda, nome, telefone):
    agenda[nome] = telefone #adiciona na lista o nome como chave e telefone valor
    return 'Contato adicionado!'

def buscar_telefone(agenda, nome):
    if nome in agenda:
        return f'{nome}: {agenda[nome]}'
    else:
        return 'Contato não encontrado'
    
def remover_contato(agenda, nome):
    if nome in agenda:
        del agenda[nome]
        return 'Contato deletado'
    else:
        return 'Contato não encontrado'
    
def listar_contato(agenda):
    for pessoas in sorted(agenda):
        print(f"{pessoas}: {agenda[pessoas]}")


# ----------------------------------------------------------


while True:
    print("(1) Adicionar contato")
    print("(2) Buscar o telefone de um contato")
    print("(3) Remover um contato")
    print("(4) Listar todos os contatos")
    print("(5) Sair do programa")

    o = input("\nDigite sua escolha aqui:")

    if o == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        adicionar_contato(agenda, nome, telefone)

    elif o == "2":
        nome = input("Nome do contato que deseja procurar: ")
        print(buscar_telefone(agenda, nome))
    
    elif o == "3":
        nome = input("Nome do contato que deseja remover: ")
        print(remover_contato(agenda, nome))
    
    elif o == "4":
        listar_contato(agenda)
    
    elif o == "5":
        print("Saindo do programa...")
        break
    
    else:
        print("Opçao invalida")
    