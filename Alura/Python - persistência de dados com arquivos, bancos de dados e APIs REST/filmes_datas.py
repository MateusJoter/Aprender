filmes = ['Missão Impossível', 'Interestelar', 'Oppenheimer', 'O Poderoso Chefão']

datas = ('1996', '2014', '2023', '1972')

dict_datas_dos_filmes = {}

for filme, data in zip(filmes, datas):
    dict_datas_dos_filmes[filme] = data

print(dict_datas_dos_filmes)

for filme, data in dict_datas_dos_filmes.items():
    print(f'O filme {filme} foi lançado em {data}')