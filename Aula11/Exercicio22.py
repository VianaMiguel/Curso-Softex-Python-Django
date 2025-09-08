jogador= [{"nome":"Davi", "pontuacao": 15},
          {"nome":"Denis","pontuacao":20}, 
          {"nome":"Luis","pontuacao":25},  
          {"nome":"João","pontuacao":5}, 
          {"nome":"Henry","pontuacao":30}]


while True:

 novo_jogador = input("Nome do Novo Jpgador: ").lower()
 nova_pontuação = int(input("Pontuação do Novo Jogador: "))

 if novo_jogador in jogador:
   jogador[nome]["pontuacao"] += pontuacao
    jogador[nome]["nome"] = nome
                print(f"Jogador {novo_jogador} inserido.").