import random

def pedra_papel_tesoura(escolha_jogador):
    escolha_computador = random.choice(["pedra", "papel", "tesoura"])
    print(f"Computador escolheu: {escolha_computador}")
    escolha_jogador = escolha_jogador.lower()

    if escolha_jogador == "pedra":
        match escolha_computador:
            case "pedra":
                return "Empate!"
            case "papel":
                return "Você perdeu!"
            case "tesoura":
                return "Você venceu!"
            
    if escolha_jogador == "papel":
        match escolha_computador:
            case "papel":
                return "Empate!"
            case "tesoura":
                return "Você perdeu!"
            case "pedra":
                return "Você venceu!"
            
    if escolha_jogador == "tesoura":
        match escolha_computador:
            case "tesoura":
                return "Empate!"
            case "pedra":
                return "Você perdeu!"
            case "papel":
                return "Você venceu!"
            
print(pedra_papel_tesoura(input("Escolha: pedra, papel ou tesoura?\n")))