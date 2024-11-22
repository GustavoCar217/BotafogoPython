# Classe base para uma conta bancária
class ContaBancaria:
    def __init__(self, titular, numero_conta, saldo=0):
        self.titular = input(f"Digite o nome do titular da conta: {titular}" , )
        self.numero_conta = input(f"Digite o numero da sua conta: {numero_conta}")
        self.saldo = saldo

    def depositar(self,):
        valor = int(input("Digite um valor para depositar:"))
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")
    
    def sacar(self):
        valor = int(input("Digite um valor para saque:"))
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido.")
    
    def exibir_saldo(self):
        print(f"Saldo atual da conta {self.numero_conta}: R${self.saldo:.2f}")

# Classe filha para incluir transferências
class ContaCorrente(ContaBancaria):
    def transferir(self, conta_destino):
        valor = int(input("Digite um valor para depositar:"))
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            conta_destino.depositar()
            print(f"Transferência de R${valor:.2f} para a conta {conta_destino.numero_conta} realizada com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido para transferência.")

# Demonstração de uso
if __name__ == "__main__":
    # Criando duas contas para simular operações
    conta1 = ContaCorrente( "", "",saldo=1000)
    conta2 = ContaCorrente("", "", saldo=500)

    # Operações básicas
    conta1.exibir_saldo()
    conta1.sacar()
    conta1.exibir_saldo()
    conta1.depositar()
    conta1.exibir_saldo()
    # Transferência
    conta1.transferir()
    conta1.exibir_saldo()
    conta2.exibir_saldo()