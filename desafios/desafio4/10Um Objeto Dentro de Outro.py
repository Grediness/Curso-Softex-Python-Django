class Motor:
    def potencia(self,potencial):
        self.pontencial=potencial
        return self.pontencial
class Carro:
    def __init__(self,modelo):
        self.modelo=modelo
        self.motor=Motor()
        
    def exibir_potencia(self):
        print(f'O modelo {self.modelo} tem uma potência de {self.motor.potencia(100)}')
carro=Carro('Fiat')
carro.exibir_potencia()