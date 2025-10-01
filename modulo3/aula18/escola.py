
from estudante import Estudante
class Escola():
    def __init__(self):
        self.lista:list[Estudante]=[]
    def adicionar_aluno(self,nome,idade:int,matricula):
        
        aluno=Estudante(nome,idade,matricula)
        self.lista.append(aluno)
        
        
        return aluno
    def mostrar_relatorio(self):
        
        for estudante in self.lista:
            
            print(f'O aluno {estudante.nome} com a idade {estudante.idade} que tem a matricula {estudante.matricula} ')
        
    

a=Escola()
b=a.adicionar_aluno('ana',18,563456)
d=a.adicionar_aluno('Pedro',45,78945)
er=a.mostrar_relatorio()

#TERMINAR EM CASA





        
    