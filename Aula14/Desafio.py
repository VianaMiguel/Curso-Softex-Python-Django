

class personagem:
    def __init__ (self, nome:str, vida:int, ataque:int,pocoes=0 ):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.pocoes = pocoes
        self.defedendo = False

    def atacar (self, alvo):
        dano =self.ataque
        if random.random() <0.2:
            dano *= 2
            print(f"Ataque Critico de {self.nome}!")
        print(f" {self.nome} ataca {alvo.nome} causando{dano} de dano.!")
        alvo.receber_dano(dano)

    def defender(self):
        