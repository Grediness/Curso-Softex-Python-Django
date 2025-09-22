class Livro:
    def capa(self,titulo,autor):
        self.titulo=titulo
        self.autor=autor
        return self.autor, self.titulo
class Biblioteca:
    acervo=[]
    def __init__(self,receber_titulo,receber_autor):
        self.receber_titulo=receber_titulo
        self.receber_autor=receber_autor
        
    def adicionar_livro(self):
        self.receber=Livro()
        
        self.acervo.append((self.receber.capa(self.receber_autor,self.receber_titulo)))
    def listar_livros(self):
        print(self.acervo)


a=Biblioteca('Capitães da Areia','Jorge Amado')
b=Biblioteca('Vidas Secas','Graciliano Ramos')

a.adicionar_livro()
b.adicionar_livro()

a.listar_livros()

