# cria uma linha de comentario usando #
# tudo que estiver depois do # na mesma linha é ignorado pelo Python

# comentário de bloco usando três aspas duplas
# serve para escrever comentários em várias linhas
"""
comentario de bloco
isto e util para 
eu descrever
alguma coisa
"""

# comentário de bloco usando três aspas simples
# também permite escrever em várias linhas
'''
isso tambem
e um comentario 
de bloco
'''

# imprime o texto "deu certo" na tela
print("deu certo")

# imprime uma mensagem pedindo para o usuário digitar algo
print("digite algo :")

# input() espera o usuário digitar algo e guarda o valor na variável "algo"
algo = input()

# mostra na tela o que o usuário digitou
print("o que tu digitou foi " , algo)

# pede para o usuário digitar um número
print("agora digite um numero :")

# recebe o valor digitado, converte para inteiro usando int() e guarda na variável num1
num1 = int(input())

# pede para o usuário digitar outro número
print("agora digite outro numero :")

# recebe o valor digitado, converte para inteiro e guarda na variável num2
num2 = int(input())

# soma num1 + num2 e mostra o resultado
print("o resultado da soma dos dois numeros e igual a : " , num1 + num2)

# subtrai num2 de num1 e mostra o resultado
print("o resultado da subtração dos dois numeros e igual a : " , num1 - num2)

# multiplica num1 por num2 e mostra o resultado
print("o resultado da multiplicação dos dois numeros e igual a : " , num1 * num2)

# faz a divisão de num1 por num2
# int() transforma o resultado em número inteiro
# % mostra o resto da divisão
print("o resultado da divisão dos dois numeros e igual a : " , int(num1 / num2) , " o resto da divisão e : " , num1 % num2)

# imprime o texto e muda o final da linha para "..." em vez de quebrar linha
print("professor ivonei " , end = "...")

# pede para o usuário digitar um novo número
print("digite um novo numero : ")

# recebe o valor digitado, converte para inteiro e guarda na variável num3
num3 = int(input())

# verifica se o número digitado é maior que 0
# se for maior que 0, ele é considerado positivo
if num3 > 0:

    # imprime que o número é positivo
    print("o numero que voce digitou e positivo")

    # verifica se o número é par
    # % 2 pega o resto da divisão por 2
    # se o resto for 0, o número é par
    if num3 % 2 == 0:

        # imprime que o número também é par
        print("o numero que voce digitou tambem é par")

    # caso contrário, o número é ímpar
    else:

        # imprime que o número também é ímpar
        print("o numero que voce digitou tambem é impar")

# se o número não for maior que 0, ele entra aqui (ou seja, é negativo ou zero)
else :

    # imprime que o número é negativo
    print("o numero que voce digitou e negativo")

    # verifica novamente se o número é par
    if num3 % 2 == 0:

        # imprime que o número também é par
        print("o numero que voce digitou tambem é par")

    # caso contrário, o número é ímpar
    else:

        # imprime que o número também é ímpar
        print("o numero que voce digitou tambem é impar")