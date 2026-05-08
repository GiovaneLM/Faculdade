#1
#2 1
#3 2 1
#4 3 2 1
#5 4 3 2 1


#forma 1
print(1)
print(2,1)
print(3,2,1)
print(4,3,2,1)
print(5,4,3,2,1)

#forma 2
for i in range(1,6):
    print(i)

#forma 3
for l in range(1,6):
    for i in range(5,0,-1):
        print(l, end=" ")
    print()

#forma 5
numero=int(input("digite o valor: "))
for i in range(1,numero+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()


#forma 6
coluna = 5
string = ""
for linha in range(1, coluna + 1):
    string = str(linha) + " " + string
    print(string)