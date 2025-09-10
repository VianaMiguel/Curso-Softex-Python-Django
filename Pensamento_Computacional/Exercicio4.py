
""" Exercício 4:

 Crie um algoritmo que leia 3 notas de um aluno, calcule a média e diga
"Aprovado" se a média for maior ou igual a 7, ou "Reprovado" se for menor que 7."""



#Recebo a primeira nota:
nota1=float(input("Digite a primeira nota: "))
#A segunda nota:
nota2=float(input("Digite a segunda nota: "))
#E a terceira nota:
nota3=float(input("Digite a terceira nota: "))
#Calculo a média das notas dividindo pelo numero de notas:
media=(nota1 + nota2 + nota3) / 3
#Se a média for maior ou igual a 7:
if media >= 7:
     #Imprimo Aprovado:
    print("Aprovado")
    #Se não, se a média for menor que 7:
else:
    #Imprimo Reprovado
    print("Reprovado")

