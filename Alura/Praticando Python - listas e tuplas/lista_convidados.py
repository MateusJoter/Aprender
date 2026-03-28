lista_convidados = ['Ana', 'Pedro', 'Carlos']

def alterar_lista():
    print(f"Lista atual de convidados: {lista_convidados}")

    novo_convidado = input("Digite o nome do novo convidado: ")

    try:
        pos = int(input("Digite a posição na qual deseja inserir o convidado: "))
    except Exception as e:
        print(f"Erro: {e}\n Processo interrompido")
        return

    lista_convidados.insert(pos - 1, novo_convidado)

    print(f"Lista atualizada de convidados: {lista_convidados}")

alterar_lista()