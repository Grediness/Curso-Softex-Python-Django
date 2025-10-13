from pessoa import Pessoa
class Estudante(Pessoa):
    def __init__(self, nome:str, idade:int,matricula:int):
        super().__init__(nome, idade)
        self.matricula=matricula
        self._materia={}
    @property
    def nota(self):
        return self._materia
    
    def adicionar_nota(self,materia:str,nota:int):
        aula=self.nota.get(materia)
        if aula:
            aula.append(nota)
        else:
            self.nota[materia]=[nota]
        return self.nota
    def __repr__(self):
        # Esta função diz ao Python como representar o objeto em texto
        return f"Estudante(Nome: {self.nome}, Idade: {self.idade}, Matrícula: {self.matricula} {self.nota})"
            


    