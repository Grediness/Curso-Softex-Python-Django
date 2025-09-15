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