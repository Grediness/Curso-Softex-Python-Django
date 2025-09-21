def cadastrar_produto(estoque:dict)-> None:
    '''Permite ao atendente cadastrar um novo produto'''
    nome_produto=input('Digite o nome do novo produto(identificador)').lower()

    if nome_produto in estoque:
        print('ERRO!!!!!')

    try:
        nome_completo=input('Digite o nome do produto:')
        valor=float(input('Digite o valor do nome produto:'))
        quant=int(input('Digite a quantidade inicial do produto:'))

        if nome_produto and valor>0 and quant>0:
            estoque[nome_produto]={'nome':nome_completo,'valor':valor,'quantidade_do_produto':quant}
            print(f'Produto {nome_completo} cadastrado com sucesso!!!')

        else:
            print('ERRO"!!!!')

    except ValueError:
        print('Entrada inválida')

def atualizar(estoque:dict)-> None:

    '''Permite ao atendente atualizar um produto existente'''

    nome_produto=input('Digite o nome do produto para atualizar (identificador):').lower()

    if nome_produto not in estoque:
        print('Produto não cadastrado')
        return
    
    print(f'Produto {estoque[nome_produto]} selecionado')
    escolha=input('O que deseja atualizar? \n 1-Valor \n 2- Quantidade \n Opção:')

    try:
        if escolha=='1':
            novo_valor=float(input('Digite o novo valor do produto:'))

            if novo_valor>0:
                estoque[nome_produto]['valor']=novo_valor
                print(f'Valor atualizado para {novo_valor:.2f}')

            else:
                print('valor inválido')

        elif escolha=='2':
            nova_quant=int(input('Digite a nova qunatidade do produto:'))

            if nova_quant>0:
                estoque[nome_produto]['quantidade']+=nova_quant
                print(f'Valor atualizado para {estoque[nome_produto]['quantidade']} itens')

            else:
                print('Quantidade inválida ')

        else:
            print('Erro!!!! OPCAO INVALIDA')

    except ValueError:
        print('ACEITAMOS APENAS NÙMEROS')