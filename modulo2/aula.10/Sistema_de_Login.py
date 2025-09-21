class Login:
    def __init__(self):
        self.acessos=[('Pedro','sucesso'),('Ana','falha'),('Maria','sucesso'),('Pedro','falha'),('Ana','falha')]
        self.verificar()
    def verificar(self):
        nome_sucesso=set()
        nome_falha=set()
        for nome,situacao in self.acessos:
            if situacao=='sucesso':
                nome_sucesso.add(nome)
            elif situacao=='falha':
                nome_falha.add(nome)
        apenas_falha=nome_falha.difference(nome_sucesso)
        print(f'Usuários com pelos menos um login bem-sucedido: {nome_sucesso}')
        print(f'Usuários que tiveram apenas falhas: {apenas_falha}')

a=Login()