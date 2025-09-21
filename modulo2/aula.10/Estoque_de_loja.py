class Loja:
    def __init__(self):
        self.estoque_principal=[('Camiseta',101),('Calça',102),('Boné',103),('Tênis',104)]
        self.estoque_online=[('Boné',103),('Camisa Polo',105),('Calça',102),('Chinelo',106)]
        self.novo_estoque_1=set(self.estoque_principal)
        self.novo_estoque_2=set(self.estoque_online)
        loja_e_site_em_comum=self.novo_estoque_1.intersection(self.novo_estoque_2)
        print(f'Os produtos em comum entre a loja e o site são:{loja_e_site_em_comum}')
        somente_loja=self.novo_estoque_1.difference(self.novo_estoque_2)
        somente_site=self.novo_estoque_2.difference(self.novo_estoque_1)

        print(f'Os itens que estão apenas na loja são:{somente_loja}')
        print(f'Os itens que estão apenas no site são:{somente_site}')
a=Loja()