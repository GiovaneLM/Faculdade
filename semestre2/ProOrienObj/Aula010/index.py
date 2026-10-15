class ContaBancaria:
    
    def __init__(self, titular, saldo):
        self.__titular = titular # Atributo privado
        self.__saldo = saldo # Atributo privado
    
    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print("Saque realizado com sucesso.")
            self.listar_saldo()
        else:
            print("Saldo insuficiente.")
    
    def depositar(self, valor):
        self.__saldo += valor
        print("Depósito realizado com sucesso.")
        self.listar_saldo()
    
    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular

    def listar_saldo(self):
        print('titular:',self.__titular)
        print('saldo:',self.__saldo)


cliente1 = ContaBancaria('Gabriel',1000.00)
#cliente1.listar_saldo()
cliente1.sacar(100)
#cliente1.listar_saldo()

##alteraçao impossivel
cliente1.__saldo=2000
print('nao funciona cliente1.__saldo=2000')
cliente1.listar_saldo()

cliente1.depositar(1200)
#cliente1.listar_saldo()