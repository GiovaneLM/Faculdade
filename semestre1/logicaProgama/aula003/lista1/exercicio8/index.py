'''8. Faça um algoritmo que leia valores para as variáveis a, b e c e mostre o resultado da expressão (a - b) * c'''

# Exibe mensagem pedindo o valor de a (num1)
print("digite o primeiro numero : ")
# Lê o valor digitado e converte para inteiro
num1 = int(input())
# Exibe mensagem pedindo o valor de b (num2)
print("digite o segundo numero : ")
# Lê o segundo valor digitado e converte para inteiro
num2 = int(input())
# Exibe mensagem pedindo o valor de c (num3)
print("digite o terceiro numero : ")
# Lê o terceiro valor digitado e converte para inteiro
num3 = int(input())
# Calcula e exibe o resultado da expressão (a - b) * c
print("o resultado do calculo (",num1," - ",num2,") x ",num3," é ", (num1 - num2)*num3)