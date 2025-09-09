"""Exercício 1: Crie um algoritmo que leia a idade de uma pessoa e diga "Você é adulto" se a
idade for 18 ou mais, ou "Você é menor de idade" se for menos que 18."""

#Recebo a idade do usuário:
idade=int(input(" Diga sua idade: "))
#Se a idade for maior ou igual a 18anos:
if idade >=18:
    #Imprimo que o usuário é adulto:
    print("Você é adulto!")
    #Se não:
else:
    #Imprimo idade for menor que 18 anos:
    print("Você é menor de idade") 