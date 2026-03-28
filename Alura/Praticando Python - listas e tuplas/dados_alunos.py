class Perfil:
    def __init__(self, aluno, idade, nota):
        self._aluno = aluno
        self._idade = idade
        self._nota = nota

    def apresentar_dados(self):
        print(f"""
            {'Aluno:'.ljust(10)}{self._aluno}
            {'Idade:'.ljust(10)}{self._idade}
            {'Nota:'.ljust(10)}{self._nota}
            """)

def dados_alunos():
    dados = input("Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: ")
    dados = dados.split(", ")
    lista_perfis = []

    for dado in range(int(len(dados)/3)):
        perfil = Perfil(dados[0], dados[1], dados[2])
        lista_perfis.append(perfil)
        dados = dados[3:]
    
    for perfil in lista_perfis:
        perfil.apresentar_dados()

dados_alunos()