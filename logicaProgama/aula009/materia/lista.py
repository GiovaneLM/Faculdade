"listas"

# lista=[]
# lista.append(n)           - adiciona no final 
# lista.remove(elemento)    - remove o primeiro elemento encontrado
# lista.pop(posicao)        - remove pela posiçao
# lista[0]=novo elemento    - altera 
# lista.index(elemento)     - posiçao na lista



# l_nomes=['ana', 'maria', 'juca', 'pedro', 'mario']
# l_idades=[22, 44, 57, 36, 68]

# while True:
#     # nome=input("nome: ")
#     # idade=int(input("idade: "))

#     # l_nomes.append(nome)
#     # l_idades.append(idade)

#     print(l_nomes)
#     print(l_idades)

#     nome_aux=input("nome para localizar: ")
#     if nome_aux in l_nomes:
#         for nome in l_nomes:
#             if nome_aux == nome:
#                 pos=l_nomes.index(nome_aux)
#                 idade=l_idades[pos]
#                 print(f"achei {nome} na posição : {pos} idade: {idade}")
#     else:
#         print("nome nao encontrado")




l_nomes=['ana', 'maria', 'juca', 'pedro', 'mario']
l_idades=[22, 44, 57, 36, 68]

try:
    l_nomes.remove("Ivone")
except:
    print("nome nao encontrado")











nome1=input("nome1: ")#l_nomes[0]
nome2=input("nome2: ")#l_nomes[3]

if nome1 in l_nomes and nome2 in l_nomes:
    ind1=l_nomes.index(nome1)
    ind2=l_nomes.index(nome2)

    nome_aux= l_nomes[ind1]
    idade_aux=l_idades[ind1]

    l_nomes[ind1] = l_nomes[ind2]
    l_nomes[ind2] = nome_aux


    l_idades[ind1] = l_idades[ind2]
    l_idades[ind2] = idade_aux
    pass
else:
    print("nao achado")


idade1=l_idades[0]
idade2=l_idades[3]

l_nomes[0] = nome2
l_nomes[3] = nome1
l_idades[0]=idade2
l_idades[3]=idade1

while True:
    print(l_nomes)
    print(l_idades)
    break