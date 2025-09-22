class Circulo:
    def __init__(self, raio: float):
        self._raio = raio

    @property
    def raio (self):
        return self.raio
    
    @raio.setter
    def raio (self,novo_raio: float)    
    if isinstance (novo_raio:float) and novo_raio >=0:
        self._raio = novo_raio
    else:
        print("digite um numero positivo")