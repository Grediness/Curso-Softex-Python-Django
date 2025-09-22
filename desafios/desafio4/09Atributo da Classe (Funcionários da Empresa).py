class Funcionario:
    percentual_bonus=1.10
    def __init__(self,nome,salario):
        self.nome=nome
        self.salario=salario
    def aplicar_bonus(self,):
        bonus=self.salario*self.percentual_bonus
        print(f'O bônus do funcionário {self.nome} que tinha o salário de R$ {self.salario} foi para R$ {bonus:.2f}')
funcionario1=Funcionario('Bianca',200)
funcionario2=Funcionario('Bruna',100)
funcionario1.aplicar_bonus()
funcionario2.aplicar_bonus()