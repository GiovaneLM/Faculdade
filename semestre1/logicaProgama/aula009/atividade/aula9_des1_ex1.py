# Desafio 01
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
#
# n = 5
# for i in range(1, n+1):
#         for j in range(i, 0, -1):
#             print(j, end=" ")
#         print()
#
#
#
#
# Desafio 02
#    #
#   ###
#  #####
# #######
#  #####
#   ###
#    #
#
# n = 4
# for i in range(1, n+1):
#         espacos = n - i
#         cerquilhas = i * 2
#         print(" " * espacos + "#" * cerquilhas)
#
# for i in range(n-1, 0, -1):
#         espacos = n - i
#         cerquilhas = i * 2
#         print(" " * espacos + "#" * cerquilhas)
#
#
#
#
# Desafio 03
#
#
#        ##
#       ####
#      ######
#     #     ##
#    ##     ###
#   ###     ####
#  ####     #####
#   ###     ####
#    ##     ###
#     #     ##
#      ######
#       ####
#        ##
#
#
# for i in range(1, 7):
#     espacos = 12 - i
#     cerquilhas = i * 2 - 1
#     print(" " * espacos + "#" * cerquilhas)
#
# for i in range(1, 7):
#     espacos = 6 - i
#     cerquilhas = i
#     espaco_interno =  11
#     print(" " * espacos + "#" * cerquilhas + " " * espaco_interno + "#" * cerquilhas)
#
# for i in range(5, 0, -1):
#     espacos = 6 - i
#     cerquilhas = i
#     espaco_interno = 11
#     print(" " * espacos + "#" * cerquilhas + " " * espaco_interno + "#" * cerquilhas)
#
# for i in range(6, 0, -1):
#     espacos = 12 - i
#     cerquilhas = i * 2 - 1
#     print(" " * espacos + "#" * cerquilhas)
#
#
#
#
#
#
#
# Faça um algoritmo que leia uma quantidade indeterminada de números (finalize quando digitado a palavra 'fim')
# No final diga:
# quantos números negativos foram digitados,
# quantos números pares,
# quantos números digitados estão no intervalo de 10 e 30, ou no intervalo de 50 e 70.
#
# negativos = 0
# pares = 0
# intervalos = 0
#
# while True:
#     entrada = input("Digite um número (ou 'fim' para encerrar): ")
#
#     if entrada.lower() == "fim":
#         break
#
#     try:
#         numero = int(entrada)
#
#         if numero < 0:
#             negativos += 1
#
#         if numero % 2 == 0:
#             pares += 1
#
#         if (10 <= numero <= 30) or (50 <= numero <= 70):
#             intervalos += 1
#
#     except ValueError:
#         print("Entrada inválida. Digite um número ou 'fim'.")
#
# print("\n=== RESULTADOS ===")
# print(f"Números negativos: {negativos}")
# print(f"Números pares: {pares}")
# print(f"Números nos intervalos (10–30 ou 50–70): {intervalos}")
#
#
#
#
#
# Exercício 2:
# Faça um algoritmo que leia o nome de 8 alunos e a quantidade de acertos de uma prova de 10 questões.
# No final diga quantos alunos obtiveram a nota superior a 70% da prova,
# A nota deve ser um inteiro entre 0 e 10.
#
# alunos = []
# acima_70 = 0
#
# for i in range(8):
#     nome = input(f"Digite o nome do aluno {i+1}: ")
#     while True:
#         try:
#             acertos = int(input(f"Digite a quantidade de acertos (0 a 10) para {nome}: "))
#             if 0 <= acertos <= 10:
#                 break
#             else:
#                 print("Valor inválido! Digite um número entre 0 e 10.")
#         except ValueError:
#             print("Entrada inválida! Digite um número inteiro.")
#
#     alunos.append([nome, acertos])
#
#     if acertos > 7:
#         acima_70 += 1
#
# print("\n=== RESULTADOS ===")
# print(f"Total de alunos com nota superior a 70%: {acima_70}")
# print("\nDetalhes:")
# for nome, acertos in alunos:
#     print(f"{nome}: {acertos} acertos")
#
#
