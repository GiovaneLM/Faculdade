'''Exercício 06.
Contar quantos números pares foram digitados'''

# ======================
# COM FOR
# ======================

# Inicializa contador de números pares
qt_pares = 0

# Inicializa contador para exibir a posição do número
contador = 1

# Repete 5 vezes
for _ in range(5):

    # Exibe mensagem pedindo o número
    print("Digite o ", contador , "° numero :")

    try:
        # Tenta ler um número inteiro
        num = int(input())

    except:
        # Caso não seja número válido
        print("nao e um numero")

        # Pula para a próxima repetição
        continue

    # Verifica se o número é par
    if num % 2 == 0:

        # Incrementa contador de pares
        qt_pares += 1

        # Avança o contador de posição
        contador += 1

    else:
        # Avança o contador de posição
        contador +=1

# Verifica se houve números pares
if qt_pares > 0:

    # Exibe quantidade de pares
    print("A quantidade de números pares é:",  qt_pares)

else:
    # Caso nenhum número par tenha sido digitado
    print("Nenhum número par foi digitado")


# Indica fim do programa
print("FIM")


# ======================
# COM WHILE
# ======================

# Reinicia contador de pares
qt_pares = 0

# Reinicia contador de posição
contador = 1

# Loop enquanto contador for menor que 6 (5 repetições)
while contador < 6:

    # Exibe mensagem pedindo o número
    print("Digite o ", contador , "° numero :")

    try:
        # Tenta ler um número inteiro
        num = int(input())

    except:
        # Caso entrada inválida
        print("nao e um numero")

    # Verifica se o número é par
    if num % 2 == 0:

        # Incrementa contador de pares
        qt_pares += 1

        # Avança contador
        contador += 1

    else:
        # Avança contador
        contador +=1

# Verifica se houve números pares
if qt_pares > 0:

    # Exibe quantidade de pares
    print("A quantidade de números pares é:",  qt_pares)

else:
    # Caso nenhum número par tenha sido digitado
    print("Nenhum número par foi digitado")