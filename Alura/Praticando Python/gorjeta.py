def calcular_gorjeta(valor_conta, percentual_gorjeta):
    valor_gorjeta = valor_conta*percentual_gorjeta/100
    total_pagar = valor_conta + valor_gorjeta
    return (valor_gorjeta, total_pagar)

valor_conta = float(input("Digite o valor da conta: "))

percentual_gorjeta = float(input("Digite o percentual de gorjeta: "))

print("\n")
(valor_gorjeta, total_pagar) = calcular_gorjeta(valor_conta, percentual_gorjeta)

print(f"Valor da gorjeta: R${valor_gorjeta}")

print(f"Valor a pagar: R$ {total_pagar}")