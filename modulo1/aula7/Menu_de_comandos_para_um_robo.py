# posicao_robo=0
# while True:
#     print('Selecione uma opcão: \n 1-Avançar \n 2-Recuar \n 3-Status \n 4-Desligar')
#     selecione=int(input('Digite a opção:'))
#     if selecione==1:
#         posicao_robo+=1
#     elif selecione==2:
#         posicao_robo-=1
#     elif selecione==3:
#         print(f'o robô está na posição {posicao_robo}')
#     elif selecione==4:
#         print('O programa acabou')
#         break
#     else:
#         print('o que você digitou está incorreto')

class robo:
    def __init__(self):
        self.posicao_robo=0
        
    def posicao_frente(self):
         self.posicao_robo +=1
    
    def posicao_tras(self):
         self.posicao_robo -=1
    def posicao(self):
        print(f' a posição do {self.posicao_robo}')
    
lugar_robo=robo()
while True:
    print('Selecione uma opcão: \n 1-Avançar \n 2-Recuar \n 3-Status \n 4-Desligar')
    selecione=int(input('Digite a opção:'))
    if selecione==1:
        lugar_robo.posicao_frente()
    elif selecione==2:
        lugar_robo.posicao_tras()
        
    elif selecione==3:
        lugar_robo.posicao()
    elif selecione==4:
        print('O programa acabou')
        break
    else:
        print('o que você digitou está incorreto')
        
    





        
        