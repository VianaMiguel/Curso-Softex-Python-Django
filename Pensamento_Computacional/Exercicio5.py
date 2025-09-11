"""Exercício 5:

 Crie um algoritmo que leia 5 números e, ao final, diga qual é o maior deles. Você
vai precisar de uma variável para guardar o maior número encontrado até o momento."""


#Recebe o primeiro valor:
maior_numero = float(input("Digite um número: "))
#Contador inicia na primeira contagem:
contador = 1
#Enquanto o contador tiver menos que 5 repetições:
while contador < 5:
    #Recebe um novo número e o coloca em loop:
    novo_numero = float(input("Digite outro número: "))
    #Se o novo número for maior que o anterior:
    if novo_numero > maior_numero:
        #Maior número é atulizado com valor do novo, recebendo com o sinal de igual:
        maior_numero = novo_numero
        #Soma mais 1 valor a contagem do while:
    contador += 1
    #Imprime o maior número salvo no final formatado com duas casas decimais.
print(f"O maior número é: { maior_numero:.2f}")