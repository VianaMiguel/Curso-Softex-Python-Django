"""EXERCICIOS - 1 

Conversor de Moedas Simples (Variáveis e input):

○ Crie um programa que peça ao usuário o valor em reais (float).
○ Calcule o valor equivalente em dólar, sabendo que 1 dólar = R$ 5,00.
○ Imprima o resultado."""

    #Conversor recebe o valor em reais:
conversor = float( input ("digite o valor em reais que deseja converter: "))
    #Calcula o valor de reais por dolar: 
valore_em_dolar = conversor /5
    #Imprime o valor já convertido na tela em U$:                               
print(f"Seu saldo em dolar é: U$ {valore_em_dolar:.2f}")
