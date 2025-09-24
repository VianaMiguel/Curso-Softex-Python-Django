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


class Estudante(Pessoa):
    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade)
        self.sobrenome = sobrenome

    def apresentar(self):
                print(f"Olá, meu nome é {self.nome} {self.sobrenome} e eu tenho {self.idade} anos.")

pessoa3= Estudante ("João", 25, "Alves")
pessoa4 = Estudante ("Maria", 30, "Silva")


list1:list[Pessoa] = ["Pessoa","Estudante"]
for pessoas in list:
     pessoas.apresentar
     
