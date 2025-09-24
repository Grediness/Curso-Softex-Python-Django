class Midia:
    def __init__(self,titulo,duracao_seg):
        self.titulo=titulo
        self.duracao_seg=duracao_seg
    
    def exibir(self):
       return print(f'o titulo {self.titulo} com a duração de {self.duracao_seg}')

class Musica(Midia):
    def __init__(self, titulo, duracao_seg,artista):
        super().__init__(titulo, duracao_seg)
        self.artista=artista
    def exibir(self):
      return  print(f'o titulo {self.titulo} com a duração de {self.duracao_seg} sendo o artista {self.artista}')
class Video(Midia):
    def __init__(self, titulo, duracao_seg,resolucao):
        super().__init__(titulo, duracao_seg)
        self.resolucao=resolucao
    
    def exibir(self):
       return print(f'o titulo {self.titulo} com a duração de {self.duracao_seg} com a resolução {self.resolucao}')


musica=Musica('a barraca',45,'Caeteano Veloso')
video=Video('a barraca',45,'4k')


albuns={}

albuns['musica']=[]
albuns['video']=[]

albuns['musica'].append(musica)
albuns['video'].append(video)
for item in albuns.values():
    for midia in item:
        midia.exibir()




