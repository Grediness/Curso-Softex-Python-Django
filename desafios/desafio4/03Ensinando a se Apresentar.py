class Pessoa:
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade
    def apresentar(self):
        print(f'Meu nome é {self.nome} e tenho {self.idade} anos')
        
ser_humano1=Pessoa('João',25)
ser_humano2=Pessoa('Maria',30)
ser_humano1.apresentar()
ser_humano2.apresentar()