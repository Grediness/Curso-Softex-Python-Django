class ContaBancaria:
    def __init__(self,titular,saldo=0):
        self.titular=titular
        self.saldo=int(saldo)
    def depositar(self,valor):
        self.valor=int(valor)
        self.novo_saldo=self.saldo+self.valor
        print(f'Seu saldo que era de R$ {self.saldo} reais passou a ser de R$ {self.novo_saldo} reais')
    def saque(self,valor):
        self.sacar=valor
        if self.sacar>self.novo_saldo:
            print('Saldo insuficiente')
        else:
            self.novo_saldo-=self.sacar
            print(f'Seu saldo agora é de R$ {self.novo_saldo} reais')
usuario=ContaBancaria('Ana')
usuario.depositar(100)
usuario.saque(110)