import random

def gerar_lista_caracteres(caracteres):
    lista = []
    for char in caracteres:
        lista.append(char)
    return lista

def gerar_senha():
    lista_maiusculos = gerar_lista_caracteres("QWERTYUIOPASDFGHJKLÇZXCVBNM")
    lista_minusculos = gerar_lista_caracteres("qwertyuiopasdfghjklçzxcvbnm")
    lista_especiais = gerar_lista_caracteres("!@#$%¨&*()_`^+{}<>:?'"+'"')
    lista_numeros = gerar_lista_caracteres("1234567890")
    lista_todos = lista_especiais + lista_maiusculos + lista_minusculos + lista_numeros

    caracteres_senha = []

    for i in range(12):
        match i:
            case 0:
                caracteres_senha.append(random.choice(lista_especiais))
            case 1:
                caracteres_senha.append(random.choice(lista_maiusculos))
            case 2:
                caracteres_senha.append(random.choice(lista_minusculos))
            case 3:
                caracteres_senha.append(random.choice(lista_numeros))
            case _:
                caracteres_senha.append(random.choice(lista_todos))
    
    random.shuffle(caracteres_senha)

    senha = ""

    for char in caracteres_senha:
        senha += char

    return senha

print(gerar_senha())
