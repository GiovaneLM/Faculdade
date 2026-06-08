'''Faça um algoritmo que leia o nome e a idade de um conjunto de nadadores a partir da idade classifica-o em uma das seguintes categorias:
infantil A = 5 - 7 anos
infantil B = 8-10 anos
juvenil A = 11-13 anos
juvenil B = 14-17 anos
adulto = maiores de 18 anos
O programa deve terminar quando o nome for = “FIM”
Após a leitura dos dados motre a quantidade de alunos em cada categoria e o percentual da categoria.
Mostre também o total de alunos de todas as categorias.'''
infantilA=0
infantilB=0
juvenilA=0
juvenilB=0
adulto=0
total=0
while True:
    nome=input('informe o nome do participante (\'fim\' para encerrar): ').lower()
    if nome == "fim":
        break
    while True:
        try:
            idade=int(input(f'informe a idade do nadador {nome}:'))
            break
        except:
            print('valor de idade invalido')
    if 5 <= idade <= 7:
        infantilA += 1
        total += 1
        print(f'Nadador {nome} inscrito com sucesso na categoria Infantil A')
    elif 8 <= idade <= 10:
        infantilB += 1
        total += 1
        print(f'Nadador {nome} inscrito com sucesso na categoria Infantil B')
    elif 11 <= idade <= 13:
        juvenilA += 1
        total += 1
        print(f'Nadador {nome} inscrito com sucesso na categoria Juvenil A')
    elif 14 <= idade <= 17:
        juvenilB += 1
        total += 1
        print(f'Nadador {nome} inscrito com sucesso na categoria Juvenil B')
    elif 18 <= idade:
        adulto += 1
        total += 1
        print(f'Nadador {nome} inscrito com sucesso na categoria Adulto')
    else:
        print('idade invalida')
print(f'quantidade total de nadadores incritos: {total}')
print(f'quantidade total de nadadores incritos na categoria Infantil A: {infantilA} o que representa {infantilA/total*100}% do total de inscrições')
print(f'quantidade total de nadadores incritos na categoria Infantil B: {infantilB} o que representa {infantilB/total*100}% do total de inscrições')
print(f'quantidade total de nadadores incritos na categoria Juvenil A: {juvenilA} o que representa {juvenilA/total*100}% do total de inscrições')
print(f'quantidade total de nadadores incritos na categoria Juvenil B: {juvenilB} o que representa {juvenilB/total*100}% do total de inscrições')
print(f'quantidade total de nadadores incritos na categoria Adulto: {adulto} o que representa {adulto/total*100}% do total de inscrições')