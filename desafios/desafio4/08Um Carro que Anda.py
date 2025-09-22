class Carro:
    def __init__(self,modelo,nivel_combustivel=0):
        self.modelo=modelo
        self.combustivel=nivel_combustivel
    def abastecer(self,litros):
        self.combustivel+=litros
    def dirigir(self,distancia):
        km=self.combustivel*5
        km_rodados=distancia*5
        if distancia>km:
            print(f'O carro {self.modelo} não tem combustível suficiente')
        else:
            self.combustivel-=km
            print(f'O carro {self.modelo} andou')

a=Carro('Fiat')
a.abastecer(4)
a.dirigir(50)