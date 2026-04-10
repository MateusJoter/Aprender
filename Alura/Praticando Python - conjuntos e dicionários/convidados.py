convidados = set()

convidado = str

while convidado != 'sair':
    convidado = input("Digite o nome do convidado: ")
    if convidado != 'sair':
        convidados.add(convidado)
        
print(f"Convidados confirmados: {', '.join(convidados)}")