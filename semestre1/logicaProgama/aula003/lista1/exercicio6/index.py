'''6. Fazer um algoritmo para ler dois números e mostrar o maior deles.'''

print("digite o primeiro numero: ")
num1 = int(input())
print("digite o segundo numero: ")
num2 = int(input())

if(num1>num2):
    print("o maior numero digitado é " , num1)
elif(num1<num2):
    print("o maior numero digitado é " , num2)
else :
    print("ambos os numeros tem o mesmo valor que é : " , num1)