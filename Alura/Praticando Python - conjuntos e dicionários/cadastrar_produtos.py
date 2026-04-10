produtos = []

quantidades = []

""" for i in range(3):
    produtos.append(input("Digite o nome do produto: "))
    quantidades.append(input("Digite a quantidade do produto: "))

dicionario_produtos = dict(zip(produtos, quantidades))

print(f"Dicionario de prdutos: {dicionario_produtos}") """

dict_prods = {
    'Caneta': '50', 
    'Caderno': '30', 
    'Borracha': '20'
    }

print(dict_prods)

item_mudar_qntd = input("Nome do produto a ser atualizado: ")

if item_mudar_qntd in dict_prods:
    dict_prods[item_mudar_qntd] = input("Nova quantidade: ")
    print(dict_prods)
else:
    print("Item não encontrado!")

print(dict_prods)