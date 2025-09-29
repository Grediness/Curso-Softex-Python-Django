class Comodo:
    def __init__(self,nome):
        self.nome=nome
class Casa:
    lista=[]
    
        
        
    def adicionar_comodo(self):
        self.comodo=Comodo()
        self.lista.append(self.comodo.nome)
    def listar_comodo(self):
        for comodom in self.lista:
            print(comodom)

a=Casa()
a.adicionar_comodo()