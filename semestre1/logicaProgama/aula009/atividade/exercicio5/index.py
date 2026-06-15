# xercício 2:
# Faça um algoritmo que leia o nome de 8 alunos e a quantidade de acertos de uma prova de 10 questões.
# No final diga quantos alunos obtiveram a nota superior a 70% da prova,
# A nota deve ser um inteiro entre 0 e 10. 


lista1=[2,5,7,1,-6]# 2,5,7,11,-6
#       0 1 3 4  5
lista2=2
lista2=5
print(lista1)
print(lista1[1])
lista1.append(9)
print(lista1)
print(lista1[1])
lista1.append(11)
print(lista1)
print(lista1[1])
lista1.insert(1,33)#insere algo na lista(posiçao , valor)
print(lista1)
print(lista1[1])
lista1.remove(11)#remove algo da lista(o elemento )
print(lista1)
print(lista1[1])
lista1.pop(1)#(posiçao )
print(lista1)
print(lista1[1])
exit()





alunos = []
acima_70 = 0

for i in range(8):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    while True:
        try:
            acertos = int(input(f"Digite a quantidade de acertos (0 a 10) para {nome}: "))
            if 0 <= acertos <= 10:
                break
            else:
                print("Valor inválido! Digite um número entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")

    alunos.append([nome, acertos])

    if acertos > 7:
        acima_70 += 1

print("\n=== RESULTADOS ===")
print(f"Total de alunos com nota superior a 70%: {acima_70}")
print("\nDetalhes:")
for nome, acertos in alunos:
    print(f"{nome}: {acertos} acertos")