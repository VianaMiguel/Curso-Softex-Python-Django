"""Adiconar contato + bucar contato + sair """

agenda={}

while True:
    print("1. Adicionar contato")
    print("2. Buscar contato")
    print("3. Sair")

    try:
        escolha = input("Digite sua opção")
        escolha = int(escolha)
    
    except ValueError:
        print("Escolha entre 1, 2 ou 3")
        continue

    if escolha == 1:
        print("Adicione nome do seu contato ")

        try:



