'''Exercício 11.
Faça um algoritmo para imprimir a seguinte figura:
#1#3#5#7#9
0#2#4#6#8#
#1#3#5#7#9
0#2#4#6#8#
#1#3#5#7#9
0#2#4#6#8#'''

# Loop externo: controla as LINHAS da “tabela”
# range(6) → 0,1,2,3,4,5 → total de 6 linhas
for linha in range(6):

    # Loop interno: controla as COLUNAS de cada linha
    # range(10) → 0 até 9 → total de 10 colunas por linha
    for coluna in range(10):

        # Aqui usamos o operador % (módulo)
        # linha % 2 → 0 se for PAR, 1 se for ÍMPAR
        # coluna % 2 → mesma lógica
        #
        # Essa condição verifica:
        # "linha é par E coluna é par"
        if linha % 2 == 0 and coluna % 2 == 0:

            # Se for par/par → imprime "#"
            # end="" impede quebrar linha → imprime tudo na mesma linha
            print("#", end="")

        # Agora verifica:
        # "linha é ímpar E coluna é ímpar"
        elif linha % 2 == 1 and coluna % 2 == 1:

            # Se for ímpar/ímpar → também imprime "#"
            print("#", end="")

        # Se não for nenhum dos dois casos acima
        else:

            # Imprime o número da coluna (0 até 9)
            # Isso acontece quando:
            # par + ímpar OU ímpar + par
            print(coluna, end="")

    # Depois de terminar todas as colunas de uma linha
    # esse print() quebra a linha (vai pra próxima)
    print()