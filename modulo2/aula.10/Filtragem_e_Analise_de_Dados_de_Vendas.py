class Dados:
    def __init__(self):
        self.vendas=[('Teclado',50,2),('Mouse',25.50,4),('Monitor',300,1),('Fone',45,1),('Webcam',75.20,2)]
        self.verificar()
    def verificar(self):
        self.nova_lista=list()
        produtos_unicos=set()
        try:
            for nome,preco,qtn in self.vendas:
            
                self.total=preco*qtn
                if self.total>=100:
                    
                        self.nova_lista.append((nome,preco,qtn))
                produtos_unicos.add(nome)
            print(self.nova_lista)
            
            
            print(produtos_unicos)
        except ValueError:
            print('O valor passdo está incorreto')
    

a=Dados()
