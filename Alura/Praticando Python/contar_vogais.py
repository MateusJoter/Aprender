def contar_vogais(frase):
    contador = 0
    for char in frase.lower():
        if char in "aeiou":
            contador += 1
    return contador

frase = input("Digite um texto: ")

qntd_vogais = contar_vogais(frase)

print(f"O texto contém {qntd_vogais} vogais.")