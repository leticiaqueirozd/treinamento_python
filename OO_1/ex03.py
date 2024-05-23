class ContaBancaria:
    def __init__(self, nome_cliente, saldo):
        self.nome_cliente = nome_cliente
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Olá {self.nome_cliente}. Saque de {valor} realizado!")
        else:
            print(f"Olá {self.nome_cliente}. Não é possível sacar, pois seu saldo é de {self.saldo}.")

conta = ContaBancaria('José', 100)
conta.depositar(50)
print(conta.saldo)   
conta.sacar(30)
print(conta.saldo)   
conta.sacar(200)     
print(conta.saldo)   
