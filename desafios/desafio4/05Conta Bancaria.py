class ContaBancaria:
    def __init__(self,titular,saldo=0):
        self.titular=titular
        self.saldo=int(saldo)
    def depositar(self,valor):
        self.valor=int(valor)
        novo_saldo=self.saldo+self.valor
        print(f'Seu saldo que era de R$ {self.saldo} reais passou a ser de R$ {novo_saldo} reais')
        
usuario=ContaBancaria('Ana',89)
usuario.depositar(100)