import random as rd
class Personagem:
    def __init__(self,nome,vida,ataque,pocoes=0):
        self.nome=nome
        self.vida=vida
        self.ataque=ataque
        self.pocoes=pocoes
        self.defendendo=False
    def atacar(self,alvo):
        dano=self.ataque
        if rd.random()<0.2:
            dano*=2
            print(f'Ataque Crítico de {self.nome}')
        print(f'{self.nome} ataca {alvo.nome} causando {dano} de dano')
        alvo.receber_dano(dano)
    def defender(self):
        self.defendendo=True

    def receber_dano(self,dano):
        if self.defendendo:
            dano=dano//2
            print(f'{self.nome} defendeu e reduziu  o dano para {dano}')
            self.defendendo=False
        self.vida -=dano
        self.vida=max(self.vida,0)
    def usar_pocao(self):
        if self.pocoes>0:
            cura=30
            self.vida
            
    