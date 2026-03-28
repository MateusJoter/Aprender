lista_corredores = ['Ana', 'Carlos', 'Pedro']

def corrigir_lista():
    nome_errado = input("Digite o nome incorreto: ")

    nome_certo = input("Digite o nome correto: ")

    if nome_errado in lista_corredores:
        idx = lista_corredores.index(nome_errado)

        lista_corredores.remove(nome_errado)

        lista_corredores.insert(idx, nome_certo)

        print(f"O nome {nome_errado} foi substituído por {nome_certo}. \nLista atualizada: {lista_corredores}")

    else:
        print("O nome incorreto não foi encontrado na lista de corredores.")
        
corrigir_lista()