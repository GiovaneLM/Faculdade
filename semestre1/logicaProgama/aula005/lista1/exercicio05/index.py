# Exercício 05.
# Verifica se um número está no intervalo entre 20 e 50

# Exibe mensagem pedindo um número inteiro
print(" \n digite um numero inteiro")

# Lê o valor digitado e converte para inteiro
num = int(input())

# Verifica se o número está entre 20 e 50 (inclusive)
if num >= 20 and num <= 50:

    # Exibe mensagem informando que está no intervalo
    print(" \n O numero digitado ", num , " esta no intervado de 20 e 50")

# Caso contrário
else:

    # Exibe mensagem informando que não está no intervalo
    print(" \n O numero digitado ", num , " não esta no intervado de 20 e 50")

# Indica fim da primeira execução
print("fim")


# Cria uma variável de controle para o laço
laco = True

# Inicia um loop que roda enquanto laco for True
while laco == True:

    # Loop interno para garantir entrada válida
    while True:

        # Exibe instruções para o usuário
        print("\n intervalo requerido 20 - 50 - numero negativo finaliza")

        try:
            # Tenta ler um número inteiro
            num = int(input(" \n digite um numero inteiro: "))

            # Sai do loop interno se a entrada for válida
            break

        # Captura erro caso o usuário não digite um inteiro
        except:

            # Informa erro de entrada
            print(" \n isso nao e um numero inteiro")

            # Continua pedindo até receber um valor válido
            continue

    # Verifica se o número é negativo (condição de saída)
    if num < 0:

        # Exibe mensagem de encerramento
        print(" \n adeus")

        # Encerra o loop principal
        break

    # Verifica se o número está entre 20 e 50 (inclusive)
    if num >= 20 and num <= 50:

        # Exibe mensagem positiva
        print(" \n O numero digitado ", num , " esta no intervado de 20 e 50")

    # Caso contrário
    else:

        # Exibe mensagem negativa
        print(" \n O numero digitado ", num , " não esta no intervado de 20 e 50")