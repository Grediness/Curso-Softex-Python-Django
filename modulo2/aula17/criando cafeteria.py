class GraoDeCafe:
    def moer(self):
        print('Os grãos de café foram moídos')
class Agua:
    def aquecer(self):
        print('A água está aquecida')
class Cafeteria:
    def __init__(self):
        self.graoCafe=GraoDeCafe()
        self.agua=Agua()
    def preparar_cafe(self):
        self.graoCafe.moer()
        self.agua.aquecer()
cafe=Cafeteria()
cafe.preparar_cafe()