class Pessoa:
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade
        print(f'Meu nome é {self.nome} e tenho {self.idade} anos')
        
ser_humano=Pessoa('João',25)
ser_humano=Pessoa('Maria',30)