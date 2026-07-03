# existe um tipo de dado no python chamado
# dicionario
# sua tarefa?
# pesquisar e montar uma explicação de o que é, e como funciona
# essa estrutura do Python
# para isso refaça o trabalho utilizado dicionario
# para isso criem grupos de ate 4 pessoas 
# ao final apresentem ao professor o que foi absorvido
# nome nota1 nota2 nota3 media conceito resultado


lista_aluno=[]
while True:
    Aluno={}
    
    nome=input("digite o nome do aluno: ")
    n1=float(input("nota1: "))
    n2=float(input("nota2: "))
    n3=float(input("nota3: "))
    media=(n1+n2*2+n3*3)/6

    if media >= 9:
        conceito = "A"
    elif media >= 7.5:
        conceito = "B"
    elif media >= 6:
        conceito = "C"
    elif media >= 4:
        conceito = "D"
    else:
        conceito = "E"

    if conceito in("A","B","C"):
        resultado = "APROVADO"
    else:
        resultado="REPROVADO"

    Aluno['nome'] = nome
    Aluno['nota1'] = n1
    Aluno['nota2'] = n2
    Aluno['nota3']  = n3
    Aluno['media'] = media
    Aluno['conceito'] = conceito
    Aluno['resultado'] = resultado


    lista_aluno.append(Aluno)
    parar = input("Deseja parar por aqui? (sim/nao): ").lower()
    if parar == "sim":
        break

for i in lista_aluno:
    print(f"nome:{i['nome']}\n1° nota:{i['nota1']}\n2° nota:{i['nota2']}\n3° nota:{i['nota3']}\nmedia:{i['media']}\nconceito:{i['conceito']}\nresultado:{i['resultado']}")