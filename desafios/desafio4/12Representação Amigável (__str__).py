class Filme:
    def __init__(self,titulo,ano,diretor):
        self.titulo=titulo
        self.diretor=diretor
        self.ano=ano
    def __str__(self):
        return f'Filme {self.titulo} ({self.ano}) -Diretor: {self.diretor}'

meu_filme=Filme('De Volta para o Futuro',1895,'Robert Zemeckis')
print(meu_filme)