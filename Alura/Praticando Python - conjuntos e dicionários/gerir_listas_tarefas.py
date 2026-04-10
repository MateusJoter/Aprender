equipe_a = {"planejar reunião", "revisar documento", "testar sistema"} 

equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"} 

# tarefas_finais = {'implementar funcionalidade', 'planejar reunião', 'revisar documento', 'corrigir bug'}

tarefas = equipe_a.union(equipe_b)

tarefas_a_serem_removidas_str = input("Digite as tarefas a serem removidas separadas por ', ': ").split(", ")

tarefas_a_serem_removidas = set(tarefas_a_serem_removidas_str)

tarefas_finais = tarefas.difference(tarefas_a_serem_removidas)

print(f"Tarefas finais: {tarefas_finais}")