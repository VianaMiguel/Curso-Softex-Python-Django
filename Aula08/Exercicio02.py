numero = input("Digite seu telefone celular: ")
    
valido = True
if numero.isdigit() and len(numero)==11:

    if valido:
        for cont1 in numero:
            contador_repetidos = 0
            for cont2 in numero:
                print(cont1 == cont2)
                if cont1 == cont2:
                    contador_repetidos +=1
                if contador_repetidos >=3:
                    print("Numero não é valido")
                    valido =  False
                    


formato = f"({numero[:2]}){numero[2:7]}-{numero[7:]}"
print(formato)