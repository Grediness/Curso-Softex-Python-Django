class Animal:
    def __init__(self,nome,idade):
        self.idade=idade
        self.nome=nome

    def som(self):
        print('Método da Super')

class Cachorro(Animal):
    def __init__(self, nome, idade,raca):
        super().__init__(nome, idade)
        self.raca=raca
    def som(self):
        print("AU AU")

class Gato(Animal):
    def __init__(self, nome, idade,especie):
        super().__init__(nome, idade)
        self.especie=especie
    
    def som(self):
        print("MIAU")

cao=Cachorro('Rex',4,'Golden')
print(cao.nome)
print(cao.idade)
print(cao.raca)
cao.som()

print()
gato=Gato('Felix',2,'Persa')
print(gato.nome)
print(gato.idade)
print(gato.especie)
