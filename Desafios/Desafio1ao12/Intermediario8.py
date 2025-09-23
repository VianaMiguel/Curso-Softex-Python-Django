""" Exercicio 8 """


class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.nivel_combustivel = 0

    def abastecer(self, litros):
        self.nivel_combustivel += litros
        print(f"Seu carro foi abastecido com {litros}L. Nível atual: {self.nivel_combustivel}L")

    def dirigir(self, distancia):
        consumo = distancia / 10 

        if consumo <= self.nivel_combustivel:
            self.nivel_combustivel -= consumo
            print(f"O carro andou {distancia} km. Combustível restante: {self.nivel_combustivel:.2f}L")
        else:
            print("Combustível insuficiente.")

carro = Carro("Fusca")
carro.abastecer(5)
carro.dirigir(30)
carro.dirigir(40)