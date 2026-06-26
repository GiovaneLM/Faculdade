#[00][00][00][00]=00
#digite um numero entre 10 e 99:

lista=[00,00,00,00]

def Soma(lista):
    return sum(lista)   
    
def Listinha():
    print(f"[ {lista[3]:02d} ] [ {lista[2]:02d} ] [ {lista[1]:02d} ] [ {lista[0]:02d} ] = {Soma(lista):02d}")

def Validar():
    while True:
        try:
            num =  int(input("digite um numero entre 10 e 99: "))
            if 10 <= num <= 99:
                return num
            print("numero invalido")
        except:
            print("Tu é lezo")

def Add_Num(num):
        lista.pop(0)
        lista.append(num)

while True:
    Listinha()
    Add_Num(Validar())

