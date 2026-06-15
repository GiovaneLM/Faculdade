'''Exercício 10.
Faça um algoritmo para imprimir a seguinte figura:
#
##
#2#
#23#
#234#
#2345#
#23456#
#234567#
#2345678#
#########'''


# Cria uma string vazia.
# Essa variável "linha" vai funcionar como uma memória que guarda os valores
# que vão sendo adicionados ao longo do loop.
# Começa vazia: ""
linha = ""


# Loop que vai de 0 até 8 (total de 9 repetições)
# A variável "coluna" assume os valores: 0,1,2,3,4,5,6,7,8
for coluna in range(0, 9):

    # Essa condição só será verdadeira quando coluna for maior que 1
    # Ou seja: começa a valer a partir do número 2
    if coluna > 1:

        # Converte o número (int) para texto (string)
        # e adiciona no FINAL da variável "linha"
        #
        # Exemplo do que acontece:
        # coluna = 2 → linha = "2"
        # coluna = 3 → linha = "23"
        # coluna = 4 → linha = "234"
        #
        # Ou seja: está "acumulando" números
        linha += str(coluna)


    # Imprime o conteúdo atual de "linha" + "#"
    #
    # Exemplos de saída ao longo do loop:
    # "" + "#" → "#"
    # "#" + "#" → "##"
    # "2" + "#" → "2#"
    # "23" + "#" → "23#"
    #
    # O "#" sempre aparece no final de cada linha
    print(linha + "#")


    # Essa condição só acontece na PRIMEIRA volta do loop (quando coluna == 0)
    if coluna == 0:

        # Aqui acontece uma mudança importante:
        # "linha" deixa de ser "" e passa a ser "#"
        #
        # Isso altera completamente o comportamento das próximas iterações
        #
        # Antes: linha = ""
        # Depois: linha = "#"
        linha = "#"


# Depois que o loop termina, "coluna" vale 8 (último valor do range)
#
# Aqui usamos multiplicação de string:
# "#" * 9 → "#########"
#
# Isso imprime uma linha final com vários "#"
print("#" * (coluna + 1))
