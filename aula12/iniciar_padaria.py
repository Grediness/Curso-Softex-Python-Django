from banco_de_dados import dados
from dados_clientes import obter_dados_cliente
from pagamento import solicitar_pagamento
from gerar_calcular import gerar_codigo_venda,calcular_frete
from atualizar_cadastrar import cadastrar_produto,atualizar
from localidade_processo import cadastrar_localidade,processar_pedido

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
