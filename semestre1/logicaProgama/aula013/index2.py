lista=[]
while True:
    for i in range(8):
        numero=int(input("numero: "))
        if len(lista) >= 8:
            lista.pop(0)
        lista.append(numero)           
        print(lista)