"""
SIMULADO.

Competências a serem observadas:
- Conhecer os comandos/funções utilizados.
- Saber utilizar os comandos/funções corretamente
- Desenvolver uma solução viável 

Faça um algoritmo que leia o nome de até 10 professores.
Cada professor da lista receberá uma nota entre 1 e 5 de uma turma com 8 alunos.
Mostre o nome do professor a soma de suas notas e também a média de notas de cada professor em ordem crescente..

Observações:
Você deverá realizar a tarefa individualmente / grupo.
Caso tenha dificuldades, pode fazer juntamente com um colega.
    - Entregue apenas um código com o nome dos participantes.
    - Indique quem desenvolveu o código

Coloque uma observação no início do código dizendo se você utilizou ou não IA na solução.
"""

# Loop principal do programa.
# O programa só vai parar quando chegar no break no final.
while True:

    # Tenta executar o código abaixo.
    # Se der erro de valor inválido, cai no except.
    try:

        # Pede a quantidade de professores e converte para inteiro.
        qtd_professor = int(input("digite quantos professores teram : "))

        # Pede a quantidade de alunos e converte para inteiro.
        qtd_aluno = int(input("digite quantos alunos teram : "))

    # Captura erro caso o usuário digite algo que não seja número.
    except ValueError:

        # Mostra mensagem de erro.
        print("valor invalido")

        # Reinicia o while principal.
        continue

    # Lista que vai armazenar os dados dos professores.
    professores = []

    # Repete conforme a quantidade de professores informada.
    for i in range(qtd_professor):

        # Pede o nome do professor.
        nome = input("qual o nome do nome professor: ")

        # Variável que vai acumular a soma das notas.
        notaF = 0

        # Loop para cadastrar as notas dadas pelos alunos.
        for j in range(qtd_aluno):

            # Loop infinito até o usuário digitar uma nota válida.
            while True:

                # Tenta converter a nota para inteiro.
                try:

                    # Pede a nota do aluno para o professor.
                    nota = int(input(f"{j+1}° Aluno Digite a nota do professoar {nome}  (entre 1 e 5): "))

                    # Verifica se a nota está dentro do intervalo.
                    if 1 <= nota <= 5:

                        # Soma a nota no total.
                        notaF += nota

                        # Sai do while porque a nota foi válida.
                        break

                    else:

                        # Mensagem caso a nota esteja fora do intervalo.
                        print('valor nao esta entre o intervalo digitado')

                        # Volta para pedir novamente.
                        continue

                # Captura qualquer erro de digitação.
                except:

                    # Mensagem de erro.
                    print('Valor invalido')

                    # Repete o loop novamente.
                    continue

        # Calcula a média do professor.
        media = notaF / qtd_aluno

        # Adiciona os dados do professor na lista.
        # Estrutura:
        # [nome, soma_das_notas, media]
        professores.append([nome, notaF, media])

        # Mostra a lista atualizada.
        print(professores)

    # Ordena os professores pela média.
    # x[2] representa a média.
    professores.sort(key=lambda x: x[2])

    # Percorre a lista dos professores.
    for l in range(qtd_professor):

        # Mostra os dados organizados.
        print(f"professor:  {professores[l][0]}  notas: {professores[l][1]}   media:  {professores[l][2]} ")

    # Mensagem final do sistema.
    print("Obrigado por usar nosso sistema \nAdeus")

    # Encerra o while principal.
    break




















# O método sort() organiza os elementos da lista.
# Nesse caso, ele vai organizar os professores pela média.

professores.sort(key=lambda x: x[2])

# -------------------- EXPLICAÇÃO DETALHADA --------------------

# Imagine que a lista professores esteja assim:

# [
#     ["Carlos", 20, 4.0],
#     ["Ana", 15, 3.0],
#     ["João", 25, 5.0]
# ]

# Cada professor é armazenado em uma lista:
# [nome, soma_notas, media]

# Índices:
# [0] -> nome
# [1] -> soma das notas
# [2] -> média

# Então:
# x[2]
# significa:
# "pegue a média desse professor"

# -------------------------------------------------------------

# O sort() funciona assim:
#
# Ele pega cada elemento da lista e compara usando a regra
# definida no key=.

# O key= serve para dizer:
# "QUAL valor deve ser usado para ordenar"

# -------------------------------------------------------------

# lambda x: x[2]

# lambda cria uma função rápida e temporária.

# Isso é equivalente a criar uma função normal:

def pegar_media(x):
    return x[2]

# E depois fazer:

professores.sort(key=pegar_media)

# -------------------------------------------------------------

# Durante a ordenação:
#
# x recebe cada professor da lista.
#
# Exemplo:
#
# x = ["Carlos", 20, 4.0]
#
# então:
#
# x[2]
#
# será:
#
# 4.0

# O sort compara essas médias para organizar a lista.

# -------------------------------------------------------------

# Resultado após ordenar:

# [
#     ["Ana", 15, 3.0],
#     ["Carlos", 20, 4.0],
#     ["João", 25, 5.0]
# ]

# Menor média -> maior média

# -------------------------------------------------------------

# Se quiser inverter:
# maior média -> menor média

professores.sort(key=lambda x: x[2], reverse=True)

# reverse=True faz a ordenação ao contrário.

# -------------------------------------------------------------

# Outros exemplos:

# Ordenar pelo nome:
professores.sort(key=lambda x: x[0])

# Ordenar pela soma das notas:
professores.sort(key=lambda x: x[1])

# -------------------------------------------------------------

# Resumindo:

# sort()  -> organiza a lista
# key=    -> define QUAL valor será usado na comparação
# lambda  -> cria uma função rápida
# x[2]    -> pega a média
# reverse=True -> inverte a ordem