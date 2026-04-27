import csv

with open('alunos.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        try:
            if row[1] != 'Nota':
                print(row[0]) if int(row[1]) >= 7 else None
        except IndexError:
            continue