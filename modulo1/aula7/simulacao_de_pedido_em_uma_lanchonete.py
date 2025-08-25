class lanchonete:
    def __init__(self,hamburguer,cupom,preco):
        self.lanche=hamburguer
        self.codigo=cupom
        self.preco=preco
        
    def verificar(self):
        valor=self.preco
        nome=input('Digite o nome do produto:')
        if nome== self.lanche:
            desconto=int(input('Você tem um cupom de desconto:') )  
            if desconto== self.codigo:
                valor=self.preco-(self.preco*0.2)
        print(f'O valor do seu {nome} é de {valor}')
produto=lanchonete('banana',1234,25)
produto.verificar()