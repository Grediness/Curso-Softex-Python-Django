class Produto:
    def __init__(self,nome,preco):
        self._nome=nome
        self._preco=preco

    @property    
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self,valor):
        if self.__verificar_valor(valor):
            self._preco=valor
        else:
            print('VALOR ERRADO')

    def __verificar_valor(self,valor):
        return valor>=0

    
caneta=Produto('caneta',150)

print(caneta.preco)
caneta.preco=10
