# Avaliação 02
# Favor salvar o código com o seu nome
# Nome: 
#
# Competências avaliadas:
# - Conhecer os comandos básicos da linguagem
# - Saber utilizar corretamente os comandos
# - Desenvolver uma solução viável e adequada para o problema proposto.
'''
Faça um algoritmo que realize a avaliação de seus professores conforme o menu abaixo.
MENU
1- cadastro de aluno
2- avaliação do Professor
3- relatório
Escolha: 

Utilize a seguinte lista de professores
lstProfessores  = [   "Ivonei Marques" ,
                    "Roberto Oliveira",
                    "Julio Carnevalle",
                    "Rafael Rehm",
                    "Fabio Giulian"
                ]
Use a seguinte lista para cadastro de alunos:
lstAlunos = []
Use a seguinte lista para dar a nota:
lstNotas  = [0,0,0,0,0]
Obs: A correlação entre lstPrefessores e lstNotas acontece pelo índice.

Na opção 1 você deverá adicionar o nome do aluno em lstAluno.
        Critérios:  - Nome não deve ter menos de 3 caracteres
                    - Nome deve ter apenas letras e espaços em branco
                    - É necessário ter alunos cadastrados antes de poder avaliar os professores.
Na opção 2  o aluno deverá dar uma nota de 1 a 5 para APENAS UM dos Professores
            escolhido pelo aluno.
        - Escolha um aluno Cadastrado   
        - Escolha um professor
        - Dar a nota ao professor (acumular a nota em lstNotas)
        Critérios:  - Validar nota. Não deixar o aluno votar mais de uma vez.
                    - A nota deve estar na faixa de 1 a 5. (1- Pior Nota,  5- Melhor Nota)
                    - Caso todos alunos já tenham votado, exibir a seguinte mensagem:
                        "Todos alunos já votaram."
Na opção 3 você deverá listar os prefessores e suas avaliações,
        calculando o percentual da nota conforme Exemplo:
        ----------------------------------------------------
        Professor                    Nota    Perc
        Ivonei Marques               34      22.5
        Roberto Oliveira             40      26.5
        Julio Carnevalle             19      12.6
        Rafael Rehm                  37      24.5
        Fabio Giulian                21      13.9
        ----------------------------------------------------
'''
lstProfessores = [
    "Ivonei Marques",
    "Roberto Oliveira",
    "Julio Carnevalle",
    "Rafael Rehm",
    "Fabio Giulian"
]

lstAlunos = []
lstVotaram = []
lstNotas = [0, 0, 0, 0, 0]


def cadastrarAluno():
    while True:
        try:
            aluno = input("Digite o nome do aluno: ").strip()
            if len(aluno) < 3:
                print("O nome deve ter pelo menos 3 caracteres.")
            elif not all(letra.isalpha() or letra.isspace() for letra in aluno):
                print("O nome deve conter apenas letras e espaços.")
            else:
                lstAlunos.append(aluno)
                print("Aluno cadastrado com sucesso!")
                break
        except:
            print("Erro ao cadastrar o aluno.")


def avaliarProfessor():
    if len(lstAlunos) == 0:
        print("Nenhum aluno cadastrado.")
        return
    if len(lstVotaram) == len(lstAlunos):
        print("Todos alunos já votaram.")
        return
    while True:
        try:
            for i in range(len(lstAlunos)):
                print(f"{i+1} - {lstAlunos[i]}")
            aluno = int(input("Escolha: ")) - 1
            if 0 <= aluno < len(lstAlunos):
                break
            else:
                print("Aluno inválido.")
        except:
            print("Digite um número válido.")
    if lstAlunos[aluno] not in lstVotaram:
        while True:
            try:
                for i in range(len(lstProfessores)):
                    print(f"{i+1} - {lstProfessores[i]}")
                professor = int(input("Escolha: ")) - 1
                if 0 <= professor < len(lstProfessores):
                    break
                else:
                    print("Professor inválido.")
            except:
                print("Digite um número válido.")

        while True:
            try:
                nota = int(input("Qual nota deseja dar ao professor (1 a 5): "))
                if 1 <= nota <= 5:
                    break
                else:
                    print("A nota deve estar entre 1 e 5.")
            except:
                print("Digite um número válido.")
        lstNotas[professor] += nota
        lstVotaram.append(lstAlunos[aluno])
    else:
        print("O aluno já deu nota para um professor.")


def relatorio():
    try:
        total = sum(lstNotas)
        print("-" * 50)
        print(f"{'Professor':25} {'Nota':>5} {'Perc':>8}")
        print("-" * 50)
        for i in range(len(lstProfessores)):
            if total > 0:
                perc = (lstNotas[i] / total) * 100
            else:
                perc = 0
            print(f"{lstProfessores[i]:25} {lstNotas[i]:>5} {perc:>7.1f}%")
        print("-" * 50)
    except:
        print("Erro ao gerar o relatório.")
'''USEI IA NESSA PARTE POIS NAO ESTAVA SABENDO COMO ALINHAR O RELATORIO'''

while True:
    try:
        menu = int(input("1- cadastro de aluno\n2- avaliação do Professor\n3- relatório\nEscolha: "))
    except:
        print("Digite uma opção válida.")
        continue
    if menu == 1:
        cadastrarAluno()
    elif menu == 2:
        avaliarProfessor()
    elif menu == 3:
        relatorio()
    elif menu == 0:
        print("Adeus")
        print("Sistema feito por: Giovane L. Martins")
        break
    else:
        print("Opção inválida.")