def analisar(frase:str):
    nova_frase: str = "".join(letra.lower() for letra in frase if letra.isalpha())
    vogal: int = 0
    conso: int = 0

    for letra in nova_frase:
        if letra in "aeiou":
            vogal += 1
        else:
            conso += 1

    return { "palavra": len(frase.split()), "vogais": vogal, "consoante": conso, "palindromo": nova_frase == nova_frase[::-1] }

frase: str = input("Digite uma frase para analise: ")
analise: dict = analisar(frase)
print("--- Resumo da Análise ---")
print("Palavras: ", analise["palavra"])
print("Vogais: ", analise["vogais"])
print("Consoantes: ", analise["consoante"])
print(" É um palindromo? ", analise["palindromo"])