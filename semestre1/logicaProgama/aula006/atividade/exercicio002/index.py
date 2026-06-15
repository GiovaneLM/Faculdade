# Faça um algoritmo que leia uma string no formato de data (dd/mm/aaaa)
# e escreva esta com o nome do mês por extenso.
# Exemplo:
# entrada: 25/04/2025
# saida : 25 de abril de 2025.

data = input("Digite a data (formato: dd/mm/aaaa): ")

dia , mes , ano = data.split("/" or " ")

if int(mes) >= 1 and int(mes) <= 12:
    if int(mes) == 1 or int(mes) == 3 or int(mes) == 5 or int(mes) == 7 or int(mes) == 8 or int(mes) == 10 or int(mes) == 12:
        if int(dia) >= 1 and int(dia) <=31:
            print("data valida")
            data_valida = True
        else:
            print("data invalida")
            data_valida = False
    elif int(mes) == 4 or int(mes) == 6 or int(mes) == 9 or int(mes) == 11:
        if int(dia) >= 1 and int(dia) <=30:
            print("data valida")
            data_valida = True
        else:
            print("data invalida")
            data_valida = False
    elif int(mes) == 2:
        if int(dia) >= 1 and int(dia) <= 28 or int(dia) >= 1 and int(dia) <= 29:
            print("data valida")
            data_valida = True
        else:
            print("data invalida")
            data_valida = False
    else:
        print("data invalida")
        data_valida = False

meses = [" ","janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
if data_valida == True:
    print("{} de {} de {}".format(dia,meses[int(mes)],ano))