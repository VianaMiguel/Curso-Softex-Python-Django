""" Exercicio 4

Verificador de Número Par: Crie uma função que receba um número e retorne True se 
ele for par e False se for ímpar. """


def par(numero:int):
    return numero % 2 == 0

print(par(23))
print(par(96))