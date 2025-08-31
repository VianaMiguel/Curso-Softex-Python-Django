"""Desafio de Programação: Validação de Triângulo
Seu objetivo: Escrever um algoritmo em Python que determine se três valores, fornecidos pelo usuário, podem formar um triângulo.

As Regras do Jogo
1- Teste se a entrada de dados é um número.
2- Se for um número teste se é positivo
3- Para que três lados (lA,lB,lC) formem um triângulo, eles devem obedecer a duas condições importantes:

A soma: A soma de quaisquer dois lados deve ser maior que o terceiro lado.

lA<lB+lC

lB<lA+lC

lC<lA+lB

A diferença: O valor absoluto da diferença entre dois lados deve ser menor que o terceiro lado.

lA>∣lB−lC∣

lB>∣lA−lC∣

lC>∣lA−lB∣

Dica: use o método abs() para ter o valor absoluto de um número."""

lado_a = (input(" Digite um valor para o lado A do triâgulo: "))
lado_b = (input(" Digite um valor para o lado B: "))
lado_c = (input(" Digite um valor para o lado C: "))

if lado_a.isdigit() and  lado_b.isdigit() and lado_c.isdigit():
    lado_a = float(lado_a)
    lado_b = float(lado_b)
    lado_c = float(lado_c)
    
    if lado_a > 0 and lado_b > 0 and lado_c >0:
        if (lado_a < lado_b + lado_c ) and (lado_b < lado_a + lado_c) and (lado_c < lado_a + lado_b) and (lado_a > abs(lado_b - lado_c)) and (lado_b > abs(lado_a - lado_c)) and (lado_c > abs(lado_a - lado_b)):
            print("Os valores podem formar um triângulo! ")
        else:
            print("Os valores não formam um triângulo! ")
    else:
        print("Digite apenas números positivos!")
else:
    print("Tente novamente, digite apenas números positivos!")