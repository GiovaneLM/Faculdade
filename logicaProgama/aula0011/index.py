#FUNÇOES



def nome_func(texto, numero):
    global v1 
    v1=222
    v2='cocacola'
    print(texto , ' gosta de ', v2)
    print(numero * 2)
    print(v1)
    return "Feito. Executei."

def nome_func2():
    def sub2():
        print('123')
    sub2()
    print('ccc')

def nome_func3():
    print('ddd')
    nome_func2()

##########################################
#programa principal
v1='batatinha frita 123'


print(v1)
nome_func('Tio Ivo', 55)
x=nome_func('Tio Ivo', 55)
print('aaa')
nome_func2()
nome_func3()
print(v1)
print(x)




def ler_string(mensagem):
    string=input(mensagem)
    return string

x=ler_string('digite seu nome: ')
print(x)
print(ler_string('digite seu endereço: '))

def ler_string(mensagem):
    return input(mensagem)

x=ler_string('digite seu nome: ')
print(x)
print(ler_string('digite seu endereço: '))


lista=[]

mensagem=['digite seu nome: ', 'digite seu endereço: ','idade: ']

for x in range(3):
    lista.append([ler_string(mensagem[x])])

print(lista)


