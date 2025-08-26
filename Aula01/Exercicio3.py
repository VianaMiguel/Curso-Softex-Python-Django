"""EXERCICIOS - 3 

Maior de Idade (Aninhamento de if):

○ Peça ao usuário o nome e a idade.
○ Se a idade for maior ou igual a 18, imprima: "Olá, [nome]! Você é maior de idade."
○ Se for menor, imprima: "Olá, [nome]! Você é menor de idade. """

#Recebo o nome do usuário:
nome_1 = input("Digite seu nome: ")
#Recebo sua idade:
idade_1 = int(input("Digite sua idade: "))
#Se a idade for maior ou igual a 18:
if idade_1 >= 18:
    #Imprimo a mensagem de confirmação de adulto:
    print(f"Olá, {nome_1}! Você é maior de idade.")
#Se não:
else:
    #usuário é menor de idade:
    print(f"olá, {nome_1} ! Você é menor de idade.")
