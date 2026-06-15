'''2. Escreva um algoritmo que leia dois números...'''

# Exibe mensagem pedindo o valor de vA
print("digite  valor de vA  :")
# Lê o valor digitado e armazena em vA
vA = int(input())
# Exibe mensagem pedindo o valor de vB
print("digite valor de vB :")
# Lê o valor digitado e armazena em vB
vB = int(input())
# Mostra os valores antes da troca
print("ANTES DA TROCA vA = ", vA, " vB = " , vB)

'''TROCAR O CONTEUDO DAS VARIAVEIS'''

'''
# Salva o valor de vA em uma variável auxiliar
aux = vA
# Coloca o valor de vB em vA
vA = vB
# Coloca o valor salvo (antigo vA) em vB
vB = aux
'''
# Troca os valores usando a sintaxe simplificada do Python
vA, vB = vB, vA  # python
# Mostra os valores depois da troca
print("DEPOIS DA TROCA vA = ", vA, " vB = " , vB)