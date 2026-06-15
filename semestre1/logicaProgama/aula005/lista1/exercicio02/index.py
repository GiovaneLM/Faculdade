'''Exercício 02.
Faça um algoritmo que imprima dez vezes o caracter "#" um ao lado do outro. Utilizando o comando for.'''

# Repete o laço 10 vezes (i vai de 0 até 9)
for i in range(10):

    # Imprime "#" na mesma linha (sem quebra de linha)
    print("#", end="")


# Repete o laço 10 vezes (usando "_" quando não precisamos da variável)
for _ in range(10):

    # Imprime "#" na mesma linha (sem quebra de linha)
    print("#" , end="")

# Imprime "fim" após os dois primeiros blocos
print("fim")


# Repete o laço 10 vezes
for _ in range(10):

    # Verifica se o valor atual é igual a 5
    if _ == 5:

        # Imprime o valor 5 seguido de ";"
        print(_ , ";")

    # Imprime "#" na mesma linha
    print("#" , end="")

# Imprime "fim" ao final
print("fim")