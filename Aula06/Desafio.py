""" Criação de um app bancario 
1 - Rodar em loop infinito
2 - Ter conta e senha (Validação)
3 - Encerrar atendimento
4 - Cheque Especial (Limitre de Saldo Negativo)
5 - Ter 3 Tentativas para acertar a Senha
6 - Opções (Saque, Deposito, Saldo)
7 - Mostrar Saldo Após o Saque
8 - Alterar Senha
9 - Dizer o Nome do Usuario (Mensagem de Bem-Vindo)
10 - Opção de Pagar Boleto
"""
# Declaração Constantes
conta_corrente = "123456-7"
senha_usuario = "9999"
saldo_atual = 0
limite_saldo_negativo = 500.00
nome_usuario = "José"

while True:
    for i in range(3):
        conta =input("Entre com a sua conta corrente: ")
        senha =input("Entre com a sua senha")
        if conta==conta_corrente and senha==senha_usuario:
            print(f"Seja Bem-Vindo {nome_usuario}")
            acesso_permitido=True
            break
        else:
            print("Usuario ou Senha Invalidos")
            acesso_permitido=False
    if not acesso_permitido:
        break

    while True:
        opcao = input("Escolha uma Opção:\n" \
        "1 - Ver Saldo.\n" \
        "2 - Sacar Valor.\n" \
        "3 - Depositar.\n" \
        "4 - Pagar Boleto.\n" \
        "5 - Alterar Senha.\n" \
        "6 - Sair.\n" \)
        
        if opcao =="1":
            print(f"Saldo atual é de {saldo_atual}.")
        elif opcao=="2":
            valor_a_sacar= float(input("entre coom o valor a ser sacado: "))
            if valor_a_sacar <= (saldo_atual + limite_saldo_negativo):
                saldo -= valor_a_sacar
                print("Saldo insuficiente!")
        elif opcao=="3":
            depositar = float(input("Insira o Valor a ser Depositado:"))
            if depositar > 0:
                saldo += despositar
            else:
                print("valor Inválido!")
        elif opcao=="4":
            boleto = float(input("Entre com o valor do boleto"))
            if boleto < (saldo_atual + limite_saldo_negativo):
                saldo -= boleto
            else:
            print("Saldo insuficiente!")
        elif opcao=="5":
            senha_antiga = input("Digite sua senha antiga: ")
            senha_nova1 = input("Digite sua nova senha:")
            senha_nova2 = input("Repita a senha nova: ")
            if senha_antiga == senha_usuario and senha_nova1 == senha_nova2:
                senha_usuario = senha_nova1
                print("Senha atualizada com sucesso!")
            else:
                print("Senha inválida!")
        elif opcao=="6":
            print("Atendimento finalizado!")
            break
        else:
        print("Opção inválida!")
