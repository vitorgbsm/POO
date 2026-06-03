produto = "Notebook"
quantidade = 3
preço = 3500

with open ("lista serialização de objetos/vendas.txt", "w") as p:
    p.write(f"Venda de {quantidade} unidades de {produto} por R${preço} cada.")