'''7. Ler 3 números e imprimi-los em ordem crescente.'''

# Exibe mensagem pedindo o primeiro número
print("digite o primeiro numero: ")
# Lê o valor digitado e converte para inteiro
num1 = int(input())
# Exibe mensagem pedindo o segundo número
print("digite o segundo numero: ")
# Lê o segundo valor e converte para inteiro
num2 = int(input())
# Exibe mensagem pedindo o terceiro número
print("digite o terceiro numero: ")
# Lê o terceiro valor e converte para inteiro
num3 = int(input())


'''
# Verifica se num1 é o maior número
if(num1>=num2 and num1>=num3):
    # Verifica se num2 é maior ou igual ao num3
    if(num2>=num3):
        # Imprime em ordem crescente
        print("a ordem crescente desses numeros é " ,num3 ," , ", num2," , ", num1)
    # Caso contrário
    else:
        # Imprime outra ordem possível
        print("a ordem crescente desses numeros é " , num2," , ", num3," , ",num1 )
# Verifica se num2 é o maior número
elif(num2>=num1 and num2>=num3):
    # Verifica relação entre num1 e num3
    if(num1>=num3):
        # Imprime em ordem crescente
        print("a ordem crescente desses numeros é " , num3," , ", num1," , ", num2)
    # Caso contrário
    else:
        # Imprime outra ordem possível
        print("a ordem crescente desses numeros é " , num1," , ", num3," , ",num2 )
# Caso num3 seja o maior
else:
    # Verifica relação entre num1 e num2
    if(num1>=num2):

        # Imprime em ordem crescente
        print("a ordem crescente desses numeros é " , num2," , ", num1," , ",num3 )
    # Caso contrário
    else:
        # Imprime outra ordem possível
        print("a ordem crescente desses numeros é " , num1," , ", num2," , ",num3 )
'''


'''
# Verifica combinação onde num1 é maior e num2 >= num3
if num1>=num2 and num1>=num3 and num2>=num3:
    # Imprime ordem crescente
    print("a ordem crescente desses numeros é " ,num3 ," , ", num2," , ", num1)
# Outra combinação possível
elif num1>=num2 and num1>=num3 and num3>=num2:
    print("a ordem crescente desses numeros é " , num2," , ", num3," , ",num1 )
# num2 é o maior e num1 >= num3
elif num2>=num1 and num2>=num3 and num1>=num3:
    print("a ordem crescente desses numeros é " ,num3 ," , ", num1," , ", num2)
# num2 é o maior e num3 >= num1
elif num2>=num1 and num2>=num3 and num3>=num1:
    print("a ordem crescente desses numeros é " , num1," , ", num3," , ",num2 )
# num3 é o maior e num2 >= num1
elif num3>=num2 and num3>=num1 and num2>=num1:
    print("a ordem crescente desses numeros é " ,num1 ," , ", num2," , ", num3)
# Último caso possível
else :
    print("a ordem crescente desses numeros é " , num2," , ", num1," , ",num3 )
'''


# Cria uma lista com os três números
lista = [num1,num2,num3]
# Ordena a lista em ordem crescente
l = sorted(lista)
# Exibe o resultado ordenado
print(l)
# Encerra o programa
exit()