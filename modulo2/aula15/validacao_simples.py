class Pessoa():
    def __init__(self,nome,idade):
        self._nome=nome
        self._idade=idade

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,validar):
        try:
            if validar.isalpha():
                validar=self._nome
                print(f'o nome {validar} NOME VÁLIDO')
            else:
                print('Seu nome é invalido')
        except:
            print('NUMERO Ñ É VALIDO')
    @property
    def idade(self):
        return self._idade
    @idade.setter
    def idade(self,validar):
        if validar>=0:
            print('valido')
        else:
            print('Ñ VALIDO')
nomes='aaaaaaaa'
a=Pessoa(nomes,12)
a.nome=123
a.idade=10
print(a.nome)
