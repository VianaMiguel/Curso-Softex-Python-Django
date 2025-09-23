"""exercicios 1 a 3 """

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

pessoa1 = Pessoa("João", 25)
pessoa2 = Pessoa("Maria", 30)

print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade}")
print(f"Nome: {pessoa2.nome}, Idade: {pessoa2.idade}")

pessoa1.apresentar()
pessoa2.apresentar()


