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