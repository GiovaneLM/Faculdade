class Conta():
    numero=0
    saldo=0
    #definição de metodo
    def abertura(self,numero,saldo):
        self.numero = numero
        self.saldo = saldo
        print('Conta Aberta com Sucesso!')
        
    def listar(self):
        print('\n************************************************************')
        print(f'Número:{self.numero}')
        print(f'Saldo:{self.saldo}')
        print('\n************************************************************')



#inicio do programa
#criar instancias dos objetos
mariana_cc=Conta()
raphael_cc=Conta()
daphine_cc=Conta()

mariana_cc.abertura(123123123,4000)
raphael_cc.abertura(435646,10000)
daphine_cc.abertura(567567,5000)


mariana_cc.listar()
raphael_cc.listar()
daphine_cc.listar()