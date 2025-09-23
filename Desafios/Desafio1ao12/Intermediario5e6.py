""" Exercicio 5 a 6"""


class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial


    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado. Novo saldo: R$ {self.saldo:.2f}")


    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso. Saldo atual: R$ {self.saldo:.2f}")
        else:
            print("Saldo insuficiente.")

conta1 = ContaBancaria("TioPatinhas", 100.00)
conta1.depositar(50.00) 
conta1.sacar(80.00) 
conta1.sacar(200.00)
