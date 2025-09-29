"""Montando um Carro"""

class Motor:
    def __init__(self):
        pass
        
    def ligar(self):
        print ("O Motor Ligou!")

class Carro:
    def __init__(self):
        self.motor = Motor()

    def ligar_carro(self):
        self.motor.ligar()
    
carroa = Carro()
carroa.ligar_carro()

