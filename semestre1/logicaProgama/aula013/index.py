lista=[]
par=[]
impar=[]

def validar(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except:
            print("TU É LEZO?")


def ler():
    for i in range(20):
        lista.append(validar(f"Digite o {i+1}° numero: "))

def separar():
    for i in lista:
        if i % 2 == 0:
            par.append(i)
        else:
            impar.append(i)

def resultado():
    print(f"numeros: {lista}")
    print(f"par: {par}")
    print(f"impar: {impar}")


ler()
separar()
resultado()

