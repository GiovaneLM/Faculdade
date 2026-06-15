'''13. Ler um número n e imprimir MENSAGEM 1, MENSAGEM 2 ou MENSAGEM 3, conforme a condição:
se n <= 10 imprima MENSAGEM 1,
se n > 10 e <= 100 imprima MENSAGEM 2
se n >100 imprima MENSAGEM 3,'''

# Exibe mensagem pedindo um número
print("digite um numero qualquer: ")
# Lê o valor digitado e converte para número decimal
n = float(input())
# Verifica se o número é menor ou igual a 10
if(n <= 10):
    # Exibe MENSAGEM 1
    print("MENSAGEM 1")
# Verifica se o número é maior que 10 e menor ou igual a 100
elif (n > 10 and n <=100):
    # Exibe MENSAGEM 2
    print("MENSAGEM 2")
# Caso o número seja maior que 100
else :
    # Exibe MENSAGEM 3
    print("MENSAGEM 3")