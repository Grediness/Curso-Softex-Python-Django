class Produto:
    def __init__(self,nome,preco):
        self.nome=nome
        self.preco=float(preco)
        print(f'O produto {self.nome} custa R$ {self.preco:.2f} reais.')
produtos=Produto('Caderno',15.50)
produtos=Produto('Caneta',3.00)