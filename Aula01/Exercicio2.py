"""EXERCICIOS - 2 

Par ou Ímpar (Operadores e if-else):

○ Peça ao usuário para digitar um número inteiro.
○ Use o operador de módulo (%) para verificar se o número é par (o resto da
divisão por 2 é 0).
○ Imprima se o número é "Par" ou "Ímpar". """

# Recebo o valor pelo usuário:
numero_inteiro = int(input("Digite um número inteiro: "))
# Faço o cálculo achar o resto do divisor:
divisor = numero_inteiro % 2
# Se o divisor tiver resto igual a 0:
if divisor == 0:
    # Imprimo a resposta como par:
    print("O número é Par")
# Se não:
else:
    # Imprimo o resultado como ímpar.
    print("O número é Ímpar")