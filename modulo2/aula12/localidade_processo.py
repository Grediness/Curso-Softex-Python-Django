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