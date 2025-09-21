class Contatos:
    def __init__(self):
        self.nomes={}
        self.lista_de_contatos=[]
    def verificar(self):
        while True:
           
                opcoes=input('Escolha uma das opções: \n 1- Adicionar contato \n 2- Buscar contato \n 3- Sair \n Escolha:')
                if opcoes=='3':
                    break
                else:
                    if opcoes=='1':
                        contato=input('Digite o nome do contato:')
                        self.nomes[contato]=input('Digite o número do contato:')
                        self.lista_de_contatos.append(self.nomes)
                    elif opcoes =='2':
                        procurar = input('Digite o nome do contato que deseja procurar:')
                        
                        if procurar in self.nomes:
                                print('Contato encontrado')
                        else:
                                print('Contato não encontrado')
                    else:
                         print('opção não encontrada')
                         continue
                
                
            
                
a=Contatos()
a.verificar()