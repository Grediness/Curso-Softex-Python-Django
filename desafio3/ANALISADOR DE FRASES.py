class Analise:
    def __init__(self,frase:str): 
        self.frase=frase
    def contar_letras(self):
        vogais='aeiou'
        cont_consoantes=0
        cont_vogais=0
        frase_sem_espacos=self.frase.lower().replace(' ','')
        for i in frase_sem_espacos:
            if i in vogais:
                cont_vogais+=1
            else:
                cont_consoantes+=1
        print(f'A frase {self.frase} contém:\n CONSOANTES: {cont_consoantes}\n VOGAIS: {cont_vogais}')
    def contar_espacos(self):
        frase_sem_espacos=self.frase.lower().strip()
        espacos=0
        for i in frase_sem_espacos:
            if i in ' ':
                espacos+=1
        if espacos>1:
            espacos+=1
        print(f'Sua palavra contém {espacos} espaços')

    def verificar(self):
        frase_sem_espacos=self.frase.lower().replace(' ','')
        indice=-1
        nova_frase=''
        for i in range(len(frase_sem_espacos),0,-1):
            nova_frase+=frase_sem_espacos[indice]
            indice-=1
        if nova_frase==frase_sem_espacos:
            print('Essa frase é um palíndromo')
        else:
            print('Essa frase NÃO é um palíndromo')

frase=input('Digite uma frase: ')
analise_de_frase=Analise(frase)
analise_de_frase.contar_espacos()
analise_de_frase.contar_letras()
analise_de_frase.verificar()

