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