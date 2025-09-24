class Pessoa:
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade
    
    def apresenta(self):
        print(f'O nome é {self.nome} e a idade {self.idade}')

class Estudante(Pessoa):
    def __init__(self, nome, idade,curso):
        super().__init__(nome, idade)
        self.curso=curso
    
    def apresenta(self):
        print(f'O nome é {self.nome} e a idade {self.idade} e é do curso {self.curso}')



pessoa=Pessoa('Bruna',45)
aluno=Estudante('Bruna',45,'ADS')
lista=[]
lista.append(pessoa)
lista.append(aluno)

for i in lista:
    i.apresenta()