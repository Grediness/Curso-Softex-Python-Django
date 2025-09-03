class Notas:
    def __init__(self):
        self.notas=[
            ('Ana',9.5),
            ('João',8.0),
            ('Maria',10.0),
            ('Pedro',7.5),
            ('Ana',10.0),
            ('Carlos',6.5)
        ]
       
        
    def analisarNota(self):
        self.primeira_nota=0
        for _, nota in self.notas:
            if nota>self.primeira_nota:
                self.primeira_nota=nota
        print(f'A maior nota alcançada é {self.primeira_nota}')
    def analisarAlunoSucesso(self):
        aluno_sucesso=[]
        for nome,nota in self.notas:
            if nota==self.primeira_nota:
                aluno_sucesso.append(nome)
        sucesso=tuple(aluno_sucesso)
        print(f'Alunos que tiraram a maior nota: {sucesso}')
    def AlunosFalha(self):
        reprovados=set()
        for nome,nota in self.notas:
            if nota<7:
                reprovados.add(nome)
        print(f'Alunos que tiveram a nota menor que 7.0:{reprovados}')
a=Notas()
a.analisarNota()
a.analisarAlunoSucesso()
a.AlunosFalha()
        
