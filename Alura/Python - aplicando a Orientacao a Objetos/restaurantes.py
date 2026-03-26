class Restaurante:
    nome = ""
    categoria = ""
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = "Da Praça"

# 1. Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
restaurante_praca.categoria = "Italiana"

# 2. Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
print(restaurante_praca.nome)

# 3. Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
if restaurante_praca.ativo:
    print("O resturante está ativo")
else:
    print("O restaurante está inativo")

# 4. Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
categoria = restaurante_praca.categoria

# 5. Altere o valor do atributo nome para 'Bistrô'.
restaurante_praca.nome = "Bistrô"

# 6. Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
restaurante_pizza = Restaurante()
restaurante_pizza.nome, restaurante_pizza.categoria = "Pizza Place", "Fast Food"

# 7. Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
print(f"A categoria do restaurante {restaurante_pizza.nome} é Fast Food") if restaurante_pizza.categoria == "Fast Food" else print(f"A categoria do restaurante {restaurante_pizza.nome} não é Fast Food")

# 8. Mude o estado da instância restaurante_pizza para ativo.
restaurante_pizza.ativo = True

# 9. Imprima no console o nome e a categoria da instância restaurante_praca.
print(f"O nome do restaurante da praça é {restaurante_praca.nome}, cuja categoria é {restaurante_praca.categoria}")