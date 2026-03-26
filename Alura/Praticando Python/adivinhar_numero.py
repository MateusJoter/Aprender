import random

def gerar_numero():
    return random.randrange(1, 101)

def verificar_numero():
    try:
        numero_usuario = int(input("Tente adivinhar o número de 1-100: "))
    except Exception as e:
        print(f"Entrada inválida: {e}\n")
        return ""

    numero_alvo = gerar_numero()

    try:
        while numero_usuario != numero_alvo:
            if numero_usuario not in range(1, 101):
                numero_usuario = int(input("Entrada inválida: Número fora do intervalo! Digite um número entre 1 e 100. "))

            elif numero_usuario < numero_alvo:
                numero_usuario = int(input("Muito baixo! Tente novamente: "))

            else:
                numero_usuario = int(input("Muito alto! Tente novamente: "))
    except Exception as e:
        print(f"Entrada inválida: {e}\n")
        return ""

    if numero_usuario == numero_alvo:
        print(f"Parabéns! Você acertou o número {numero_alvo}.")

verificar_numero()