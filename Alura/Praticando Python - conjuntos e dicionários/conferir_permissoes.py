permissoes_principais_str = "leitura, escrita, execução, compartilhamento"

permissoes_caso_1_str = "leitura, escrita"

permissoes_caso_2_str = "leitura, exclusão"

permissoes_principais = set(permissoes_principais_str.split(", "))
permissoes_caso_1 = set(permissoes_caso_1_str.split(", "))
permissoes_caso_2 = set(permissoes_caso_2_str.split(", "))

casos = [permissoes_caso_1, permissoes_caso_2]

for caso in casos:
    if caso.issubset(permissoes_principais):
        print("As permissões solicitadas fazem parte das permissões principais.")
    else:
        print("As permissões solicitadas não fazem parte das permissões principais.")