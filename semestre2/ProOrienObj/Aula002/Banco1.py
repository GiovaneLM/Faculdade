#definição da classe(PRIMEIRA LETRA EM MAIUSCULO)
class Conta:
    #definição dos atributos
    numero = 0
    saldo = 0.0

#inicio do Programa
#criação dos objetos
mariana_conta=Conta()
mariana_conta.numero=123123123
mariana_conta.saldo=4000.00


raphael_conta=Conta()
raphael_conta.numero=545456
raphael_conta.saldo=10000.00

daphine_conta=Conta()
daphine_conta.numero=3450956
daphine_conta.saldo=5000.00
#transferencia de uma conta para outra

raphael_conta.saldo-=100
mariana_conta.saldo+=100
print('********** Conta Maria**********')
print(f'{mariana_conta.numero} {mariana_conta.saldo}')

print('\n********** Conta Raphael**********')
print(f'{raphael_conta.numero} {raphael_conta.saldo}')

raphael_conta.saldo-=100
daphine_conta.saldo+=100
mariana_conta.saldo-=100
daphine_conta.saldo+=100

print('********** Conta Maria**********')
print(f'{mariana_conta.numero} {mariana_conta.saldo}')

print('\n********** Conta Raphael**********')
print(f'{raphael_conta.numero} {raphael_conta.saldo}')

print('\n********** Conta Daphine**********')
print(f'{daphine_conta.numero} {daphine_conta.saldo}')