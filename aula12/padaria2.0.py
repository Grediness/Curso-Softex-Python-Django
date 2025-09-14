def dados() -> dict:
    '''Carregar e retornar os dados de produtos,frete e funcionários'''
    return{
        'atendente':'Maria',
        'paes':{
            'frances':{'nome':'Pão Francês','valor':0.50,'quant':15},
            'doce':{'nome':'Pão Doce','valor':5.00,'quant':20},
            'forma':{'nome':'Pão Forma','valor':5.99,'quant':18}
        },
        'bairros':{
            'barroco':{'nome':'Barroco','frete':5.00},
            'sao jose':{'nome':'São José','frete':15},
        },
        'código de venda base':9587
    }

def obter_dados_cliente() -> dict:
    '''Solicitar e retornar os dados do cliente'''
    nome=input('Informe o seu nome:')
    return{'nome':nome}
def solicitar_pagamento() -> str:
    '''Solicitar e retornar a forma de pagamento escolhida'''
    while True:
        pagamento=input('Escolha a forma de pagamento (1-Dinheiro, 2-Cartão :)')
        if pagamento=='1':
            return 'Dinheiro'
        if pagamento=='2':
            return 'Cartão'
        else:
            print('Forma de pagamento inválida')
def gerar_codigo_venda(codigo_base:int)-> int:
    '''Gerar e retornar o código de venda'''
    return codigo_base +1
def calcular_frente(bairros_disponiveis:dict) -> tuple[str,float] | None:
    '''Calcula o valor do frete com base no bairro de entrega'''
    print('Bairros para entregas:')
    while True:
        for bairro in bairros_disponiveis.values():
            print(f'{bairro['nome']}')
        bairro_entrega_nome=input('Qual o bairro de entrega?').lower().strip()
        bairro_encontrado=None
        for chave,bairro in bairros_disponiveis.values():
            if bairro['nome']==bairro_entrega_nome:
                bairro_encontrado=chave
                break
        if not bairro_encontrado:
            print('Bairro fora da área de entrega')
        else:
            frete=bairros_disponiveis[bairro_encontrado]['frete']
            return bairro_entrega_nome,frete
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