'''9. Faça um algoritmo que mostre o resultado da expressão ((x - 5) * y) - z'''

# Exibe mensagem pedindo o valor de x
print("digite o primeiro numero : ")
# Lê o valor digitado e armazena em x
x = int(input())
# Exibe mensagem pedindo o valor de y
print("digite o segundo numero : ")
# Lê o valor digitado e armazena em y
y = int(input())
# Exibe mensagem pedindo o valor de z
print("digite o terceiro numero : ")
# Lê o valor digitado e armazena em z
z = int(input())
# Calcula e exibe o resultado da expressão ((x - 5) * y) - z
print("o resultado do calculo ((", x ," - 5) x ", y ,") - ", z ," é ", ((x - 5)*y)-z)