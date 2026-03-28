voluntarios = []

def processo_voluntarios():
    entrada = ""

    while entrada != "sair":
        entrada = input("Digite o nome do voluntário (ou 'sair' para encerrar): ")
        voluntarios.append(entrada) if entrada != "sair" else None

    print(voluntarios)

processo_voluntarios()