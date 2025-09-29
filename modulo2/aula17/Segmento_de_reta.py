import math

class Ponto:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class SegmentoDeReta:
    def __init__(self,ponto1,ponto2):
        self.ponto=Ponto(ponto1,ponto2)
    def calcular_comprimento(self):
        resultado=math.dist([self.ponto.x,self.ponto.y],[self.ponto.x,self.ponto.y])
        print(f'O pontoX {self.ponto.x} e o pontoY {self.ponto.y} sua distância é {resultado}')

a=SegmentoDeReta(2,1)
a.calcular_comprimento()