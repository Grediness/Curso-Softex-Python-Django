# class Animal:
#     def __init__(self,nome):
#         self.nome=nome
#     def __str__(self):
#         return f'Eu sou o {self.nome}'
# animal=Animal('rex')
# print(animal)
class Produto:
    def __init__(self,nome,preco):
        self._nome=nome
        self.__preco=preco
    def get_preco(self):
        return self.__preco
    def set_preco(self,valor):
        if self.__verificar_valor(valor):
            self.__preco=valor
        else:
            print('VALOR ERRADO')

    def __verificar_valor(self,valor):
        return valor>=0

    
caneta=Produto('caneta',150)
caneta.set_preco(100)
print(caneta.get_preco())
