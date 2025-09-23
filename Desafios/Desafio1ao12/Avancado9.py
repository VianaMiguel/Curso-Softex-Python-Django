""" Exercicio 9"""

class Funcionario:
    percentual_bonus = 1.10

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aplicar_bonus(self):
        self.salario *= Funcionario.percentual_bonus

funcionario1 = Funcionario("Arthur", 1500)
funcionario2 = Funcionario("Zico", 3000)


funcionario1.aplicar_bonus()
funcionario2.aplicar_bonus()

print(f"{funcionario1.nome} - R$ {funcionario1.salario:.2f}")
print(f"{funcionario2.nome} - R$ {funcionario2.salario:.2f}")