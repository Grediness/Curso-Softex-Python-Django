"""
Comercio Padaria
1- O Programa tem que rodar em loop infinito
2-Cliente pedir um tipo (francês,doce,forma,australiano)
3-Cada pão terá uma quantidade
4-Valor do pão
5-Pedir forma de pagamento (dinheiro,cartão)
6forma de entrega
7-dados do cliente(se for entregar)
8-valor do frente bairro 
9-Nome do atendente
10-Codigo da entrega
"""
nome_FRACES='Pão francês'
nome_DOCE='Pão doce'
nome_FORMA='Pão forma'

valor_FRACES=5.00
valor_DOCE=5.00
valor_FORMA=5.99    

quant_frances=15
quant_doce=20
quant_forma=18

nome_atendente='Maria'

bairro_barroco='barroco'
bairro_sao_jose='são jose'

frete_barroco=5.00
frete_sao_jose=15.00

codigo_venda=98568

while True:
    print(f'-- Bem vindo a Padaria do Desespero soua atendente {nome_atendente} --')
    escolha=input(f'temos os pães: {nome_FRACES}, {nome_DOCE}, {nome_FORMA}. Qual você deseja?')
    if escolha == nome_FRACES:
        quant=int(input('Quantos pães você deseja?:'))
        if quant <= quant_frances:
            quant_frances -= quant
            pedido_de_paes=quant
            valor_compras=quant*valor_FRACES
            print(f'Seu pediddo ficou em R$ {valor_compras}')
        else:
            print(f'Infelizmente só tenho {quant_frances} pães franceses disponíveis.')
            break
    forma_retirada=input('é para retirar na padaria ou entregar?:')
    if forma_retirada=='2':
        bairro_entregar=input(f'Qual o bairro? 1: ({bairro_sao_jose}), 2:({bairro_barroco})')
        if bairro_entregar=='1':
            valor_frete=frete_barroco
            print(f'Valor do frete R$ {valor_frete}')
            
        elif bairro_sao_jose=='2':
            valor_frete=frete_sao_jose
            print(f'Valor do frete R$ {valor_frete}')
        else:
            print('Fora da área de entrega')
            break
    elif forma_retirada=='1':
        valor_frete=0
    else:
        break
    dados_clientes=input('Informe o seu nome: ')
    forma_pagamento=input('Escolha a forma de pagamento (1-dinheiro, 2-cartão): ')
    if forma_pagamento=='1':
        forma_pagamento='Dinheiro'
    else:
        forma_pagamento='Cartão'
    codigo_atual=codigo_venda=+1
    print(f'O valor total da sua compra foi de R$ {valor_compras+valor_frete}')
    break