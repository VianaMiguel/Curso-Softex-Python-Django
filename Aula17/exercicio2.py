
class GraoDeCafe:
    def __init__ (self):
        pass

    def moer (self):
        print("Os grãos de café foram moídos.")

class Agua:
    def __init__(self):
        pass

    def aquecer (self):
        print("A água está aquecida.")

class Cafeteira:
    def __init__(self):
        self.grao = GraoDeCafe()
        self.agua = Agua()

    def preparar_cafe (self):
        self.grao.moer()
        self.agua.aquecer()

cafe = Cafeteira()
cafe.preparar_cafe()