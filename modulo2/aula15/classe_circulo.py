class Circulo:
    def __init__(self,raio):
        self._raio=raio
    @property
    def raio(self):
        return self._raio
    
    @raio.setter
    def raio(self,numero):
        if isinstance(numero,int) and numero>0:
            self._raio=numero
        else:
            print('ERRADO')

    def calcular(self):
        area=3.14*self.raio**2
        print(f'A area é de {area}')
a=Circulo(2)
print(a)
a.calcular()
