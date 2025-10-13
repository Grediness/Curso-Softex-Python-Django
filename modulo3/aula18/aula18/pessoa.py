class Pessoa:
    def __init__(self,nome:str,idade:int):
        self._nome=nome
        self.idade=idade
    @property
    def nome(self):
        return self._nome
    
