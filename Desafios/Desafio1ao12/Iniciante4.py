""" Exercicio 4"""

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

caderno = Produto("Caderno", 15.50)
caneta = Produto("Caneta", 3.00)

print(f"Produto: {caderno.nome}, Preço: R${caderno.preco:.2f}")
print(f"Produto: {caneta.nome}, Preço: R${caneta.preco:.2f}")
