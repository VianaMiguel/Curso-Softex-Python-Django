"""Dispositivo de um Computador"""

class Teclado:
    def __init__(self):
        pass

    def ligar(self):
        print("O teclado foi ativado.")

class Mouse:
    def __init__(self):
        pass

    def ligar(self):
        print("O Mouse foi ativado")

class Monitor:
    def __init__(self):
        pass

    def ligar(self):
        print("O Mouse foi ativado")

class Computador:
    def __init__(self):
        self.teclado()
        self.mouse()
        self.monitor()

    def ligar_computador(self):
        self.teclado.ligar()
        self.mouse.ligar()
        self.monitor.ligar()

pc = Computador()
pc.ligar_computador()
