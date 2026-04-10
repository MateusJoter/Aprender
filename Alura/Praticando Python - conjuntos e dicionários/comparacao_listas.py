lista_laura_str = "leite, pão, café, açúcar"

lista_ana_str = "pão, café, biscoito, chocolate"

lista_laura = set(lista_laura_str.split(", "))
lista_ana = set(lista_ana_str.split(", "))

print(f"Itens em comum: {', '.join(lista_laura.intersection(lista_ana))}")

print(f"Itens exclusivos de Laura: {', '.join(lista_laura.difference(lista_ana))}")

print(f"Itens exclusivos de Ana: {', '.join(lista_ana.difference(lista_laura))}")