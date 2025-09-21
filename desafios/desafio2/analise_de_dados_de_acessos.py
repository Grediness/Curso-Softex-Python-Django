
class Dados:
    def __init__(self):
        self.soma=0
        self.registros=[]
        self.sucessos=set()
    def verificar(self):
        while True:
            nome_ou_saida=input("Digite o nome do usuário (ou 'parar' para sair):").lower()
            if nome_ou_saida=='parar':
                break
            else:
                if not nome_ou_saida.isalpha():
                    print('Por favor digite um nome.')
                else:
                    
                    opcao=input('Selecione um dos Status \n 1-Sucesso \n 2-Falha \n Opcão:')
                    num_validos=['1','2']
                    for i in num_validos:
                        if i  in opcao :

                            try:
                                self.sessao=int(input('Digite o valor da sessão em minutos:'))
      
                            except:
                                print('O valor inserido está incorreto')
                                continue
                            if opcao=='1':
                                self.soma+=self.sessao
                                situacao='Sucesso'
                                self.sucessos.add(nome_ou_saida)
                            elif opcao=='2':
                                situacao='Falha'
                        else:
                            continue

                        dados_finais=(nome_ou_saida,situacao,self.sessao)    
                        self.registros.append(dados_finais)  
        print('Registros de acessos:')  
        print(self.registros)
        print()
        print('Usuários com acesso bem-sucedido:')
        print(self.sucessos)
        print()
        print(f'O tempo total das sessões bem-sucedidas foi de {self.soma} minutos')                
                    
a=Dados()
a.verificar()
