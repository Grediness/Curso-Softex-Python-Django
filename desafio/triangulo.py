"""
Desafio de Programação: Validação de Triângulo
Seu objetivo: Escrever um algoritmo em Python que determine se três valores, fornecidos pelo usuário, podem formar um triângulo.

As Regras do Jogo
1- Teste se a entrada de dados é um número.
2- Se for um número teste se é positivo
3- Para que três lados (lA,lB,lC) formem um triângulo, eles devem obedecer a duas condições importantes:
"""
class triangulo:
    def verificacao(self,lado_A,lado_B,lado_C):
       print('Os números são capazes de ser tornar um triângulo') if lado_A<lado_B + lado_C and lado_B<lado_A + lado_C and lado_C<lado_A + lado_B and lado_A>lado_B - lado_C and lado_B>lado_A - lado_C and lado_C>lado_A - lado_B else print('Os números não são capazes de ser tornar um triângulo')

n1=int(input('Digite o primeiro número:')) 
n2=int(input('Digite o segundo número:'))  
n3=int(input('Digite o terceiro número:'))  

numeros=triangulo()
numeros.verificacao(n1,n2,n3)
        
            