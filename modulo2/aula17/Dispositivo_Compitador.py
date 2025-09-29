class Teclado:
    def ligar(self):
        print('O teclado ligou')

class Mouse:
    def ligar(self):
        print('O mouse ligou')

class Monitor:
    def ligar(self):
        print('O monitor ligou')

class Computador:
    def __init__(self):
        self.teclado=Teclado()
        self.mouse=Mouse()
        self.monitor=Monitor()
    def ligar_computador(self):
        self.teclado.ligar()
        self.mouse.ligar()
        self.monitor.ligar()

computador=Computador()
computador.ligar_computador()