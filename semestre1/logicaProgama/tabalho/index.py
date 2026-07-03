# Escrever um algoritmo que leia, para um número não determinado de alunos, as 3 notas obtidas por cada aluno.
# Calcular a média de aproveitamento, usando a fórmula:
# media = ( Nota1 + Nota2 x 2 + Nota3 x 3 ) / 6

# A atribuição de conceitos obedece a tabela abaixo:
# Média de Aproveitamento - Conceito
# 9,0 e <= 10,0                         - A
# 7,5 e < 9,0                             - B
# 6,0 e < 7,5                             - C
# 4,0 e < 6,0                             - D
# < 4,0                                      - E
# O algoritmo deve escrever o número do aluno, suas notas, a média de aproveitamento, o conceito correspondente e a mensagem: APROVADO se o conceito for A,B ou C e REPROVADO se o conceito for D ou E.


def ler_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            return nota
        except:
            print("Erro!")


def calcular_media(n1, n2, n3):
    return (n1 + n2 * 2 + n3 * 3) / 6


def calcular_conceito(media):
    if media >= 9:
        return "A"
    elif media >= 7.5:
        return "B"
    elif media >= 6:
        return "C"
    elif media >= 4:
        return "D"
    else:
        return "E"


def calcular_resultado(conceito):
    if conceito in ("A", "B", "C"):
        return "APROVADO"
    return "REPROVADO"


def mostrar_alunos(alunos):
    for i in range(len(alunos)):
        print(f"{i+1}° Aluno")
        print(f"Média: {alunos[i][0]}")
        print(f"Conceito: {alunos[i][1]}")
        print(f"Resultado: {alunos[i][2]}")
        print("-" * 20)


Alunos = []

while True:
    Nota1 = ler_nota("Digite a 1° nota: ")
    Nota2 = ler_nota("Digite a 2° nota: ")
    Nota3 = ler_nota("Digite a 3° nota: ")

    media = calcular_media(Nota1, Nota2, Nota3)
    conceito = calcular_conceito(media)
    resultado = calcular_resultado(conceito)

    Alunos.append([media, conceito, resultado])

    parar = input("Deseja parar por aqui? (sim/nao): ").lower()

    if parar == "sim":
        break

mostrar_alunos(Alunos)