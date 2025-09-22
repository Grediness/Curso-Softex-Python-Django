class Retangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def calcular_area(self):
        self.area=self.base*self.altura
        print(f'A área de {self.base} e {self.altura} é de {self.area}')
    def calcular_perimetro(self):
        perimetro=2*(self.base+self.altura)
        print(f'O perimetro é de {perimetro}')
calculo=Retangulo(2,3)
calculo.calcular_area()
calculo.calcular_perimetro()
