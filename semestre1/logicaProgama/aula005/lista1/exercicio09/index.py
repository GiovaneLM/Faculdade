#Exercício 09.
#Faça um algoritmo para imprimir a seguinte figura:
#1
#12
#123
#1234
#12345


# Loop externo → controla QUANTAS linhas serão impressas
# range(1, 6) = 1, 2, 3, 4, 5 → total de 5 linhas
for linha in range(1, 6):

    # Loop interno → controla o que vai ser impresso em CADA linha
    # range(1, linha+1) depende da linha atual
    # Exemplo:
    # linha = 1 → range(1,2) → imprime: 1
    # linha = 2 → range(1,3) → imprime: 1 2
    # linha = 3 → range(1,4) → imprime: 1 2 3
    for coluna in range(1, linha + 1):

        # print sem quebrar linha (end="")
        # Isso faz os números ficarem lado a lado: 123
        print(coluna, end="")

    # Esse print() vazio quebra a linha depois de terminar cada linha
    print()

    # Cria uma variável vazia que vai "guardar" os números
linha = ""

# Loop de 1 até 5
for coluna in range(1, 6):

    # Converte o número para string e adiciona no final
    # Exemplo passo a passo:
    # "" + "1" = "1"
    # "1" + "2" = "12"
    # "12" + "3" = "123"
    linha = linha + str(coluna)

    # Imprime o valor atual da string
    print(linha)


    # Lê quantas linhas o usuário quer
qt_linhas = int(input("Linhas: "))

# Loop externo vai de 1 até qt_linhas (inclusive)
# Por isso usamos +1
for linha in range(1, qt_linhas + 1):

    # Mesmo conceito da versão 1
    for coluna in range(1, linha + 1):

        print(coluna, end="")

    print()