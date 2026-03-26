class Livro:
    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f"O livro'{self._titulo}' foi escrito por {self._autor} em {self._ano_publicacao}!"
    
    def emprestar(self):
        if self._disponivel:
            self._disponivel = False
            return f"Você emprestou o livro '{self._titulo}'."
        else:
            return f"Desculpe, o livro '{self._titulo}' não está disponível no momento."
        
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if ano == livro._ano_publicacao and livro._disponivel]
        return livros_disponiveis
