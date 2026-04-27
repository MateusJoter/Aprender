import csv

alunos = ['Mateus', 'Ana', 'Pedro', 'Maria']
notas = [10, 4, 1, 8]

with open('alunos.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Aluno', 'Nota'])
    f.close()

with open('alunos.csv', 'a') as f:
    for i in range(len(alunos)):
        writer = csv.writer(f)
        writer.writerow([alunos[i], notas[i]])