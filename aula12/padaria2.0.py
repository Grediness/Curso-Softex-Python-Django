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
        'código_de_venda_base':9587
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
def calcular_frete(bairros_disponiveis:dict) -> tuple[str,float] | None:
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

def cadastrar_localidade(bairros: dict) ->None:
    '''PERMITE AO ATENDENTE CADASTRAR UM NOVO BAIRRO PRA ENTREGAR'''
    nome_bairro=input('Digite o nome do Bairro (identificador)').lower().strip()
    
    if nome_bairro in bairros:
        print('ERRO!BAIRRO JÁ CADASTRADO')
        return
    
    try:
        nome_completo=input('Digite o nome completo do Bairro:').strip()
        valor_frete=float(input(f'Digite o valor de frete para o bairro {nome_completo}:'))

        if nome_bairro and valor_frete>=0 and nome_completo:
            bairros[nome_bairro]={'nome':nome_completo, 'frete':valor_frete}
            print(f'Localidade {nome_completo} com frete de R$ {valor_frete:.2f} cadastrado com sucesso!')

        else:
            print('DADOS INVÁLIDAS')
            
    except ValueError:
        print('ENTRADA INVÁLIDA!!!')

def processar_pedido(paes_disponiveis:dict) -> tuple[dict,int,float,dict]| None:
    '''PROCESSO PEDIDO DO CLIENTE,VERIFICA O ESTOQUE E CALCULA O FRETE
    RETORNAR UM ATUPLA COM O DICIONARIO DO PAO,QUANT.,VALOR TOTAL DA COMPRA E O DICIONARIO ATUALIZADO DE PAES'''
    print('Temos os seguintes pães:')

    for pao in paes_disponiveis.values():
        print(f'-{pao['nome']}') 
    escolha_pao=input('qual pão você deseja?:').lower()
    pao_encontrado=''

    for chave,paes in paes_disponiveis.items():

        if paes['nome'].lower() ==escolha_pao:
            pao_encontrado=chave
            break

    if not pao_encontrado:
        print('OPÇÃO INVÁLIDA!!')
        return
    
    pao_escolhido=paes_disponiveis[pao_encontrado]

    try:
        quant=int(input(f'Digite a quantidade do {pao_escolhido['nome']}:'))

        if quant<=0:
            print('QUANTIDADE INVÁLIDA')
            return
        
    except ValueError:
        print('ERRO!!!! QUANTIDADE DEVE SER UM NÚMERO INTEIRO')

    if quant> pao_escolhido['quant']:
        print(f' Infelizmete só tenho {pao_escolhido['quant']} unidades deste pão')
        return
    
    paes_disponiveis[pao_encontrado]['quant']-=quant
    valor_compra=quant * pao_escolhido['valor']
    return pao_escolhido,quant,valor_compra,paes_disponiveis

def iniciar_programa() -> None:
    '''FUNÇAO QUE INICIA O LOOP PRINCIPAL DO PROGRAMA DE VENDAS'''
    banco_dados=dados()
    atendente=banco_dados['atendente']
    paes_estoque=banco_dados['paes']
    bairros_disponiveis=banco_dados['bairros']
    codigo_venda=banco_dados['código_de_venda_base']
    
    while True:
        print(f'-- Bem Vindo(a) a Padaria Desespero,sou o(a) atendente {atendente}')
        print('--Menu Pricipal')
        print('1. INICIAR VENDAS')
        print('2. GERENCIAR PRODUTOS')
        print('3. CADASTRAR NOVA LOCALIDADE')
        print('4. SAIR DO SISTEMA')

        opcao=input('ESCOLHA A SUA OPÇÃO')

        if opcao=='1':
            pedido=processar_pedido(paes_estoque)

            if not pedido:
                continue

            pao_escolhido,qtd_pedido,valor_compra,paes_estoque=pedido
            print(f" Seu pedido foi de {qtd_pedido} {pao_escolhido['nome']} ficou em R$ {valor_compra:.2f}.")
            forma_retirada=input('É para 1.Retirar ou 2. Entregar?:')
            valor_frete=0.0

            if forma_retirada=='2':
                bairro,valor_frete=calcular_frete(bairros_disponiveis)
                print(f'Valor do frete para o bairro {bairros_disponiveis[bairro]['nome']} é de R$ {valor_frete:.2f}')
            elif forma_retirada !='1':
                print('OPÇÃO INVÁLIDA!!!!')
            dados_clientes=obter_dados_cliente()
            forma_pagamente=solicitar_pagamento()
            valor_total_compra=valor_frete+valor_compra
            cod_venda=gerar_codigo_venda(codigo_venda)
            banco_dados['código_de_venda_base']=cod_venda

            print('-- Resumo da venda--')
            print(f'Cliente:{dados_clientes['nome']}')
            print(f'Valor dos pães: R$ {valor_compra:.2f}')
            print(f'Valor do frete: R$ {valor_frete:.2f}')
            print(f'Forma de pagamento: {forma_pagamente}')
            print(f'Valor total da compra: R$ {valor_total_compra}')
            print(f'Código da entrega: {codigo_venda}')
        elif opcao=='2':
            pass
        elif opcao=='3':
            pass
        elif opcao=='4':
            pass













