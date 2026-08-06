def soma(n1,n2):
    return (n1+n2)

def sub(n1,n2):
    return (n1-n2)

def div(n1,n2):
    return (n1/n2)

def mul(n1,n2):
    return (n1*n2)


operacao=['+','-','/','*']
continua="S"
while True:
    if continua !='S' and continua !='SIM':
        print('Adeus👍')
        break
    while True:
        try:
            op='k'
            n1=float(input('Digite um numero: '))
            while op not in operacao:
                op=input('Digite uma operação ( + , - , / , * ): ')
            n2=float(input('Digite um numero: '))
            break
        except:
            print("digite um numero valido")
    if op == '+':
        print(f'soma {n1} + {n2} = {soma(n1,n2)}')
    if op == '-':
        print(f'subtração {n1} - {n2} = {sub(n1,n2)}')
    if op == '/':
        print(f'divisão {n1} / {n2} = {div(n1,n2)}')
    if op == '*':
        print(f'multiplicação {n1} * {n2} = {mul(n1,n2)}')

    continua=input("Continua (S/N): ").upper()