missoes=[]
recompensa=[]
nome=""
pontos=0
nome=input("ola usuario nos informe seu nome: ")

while True:
    print(f'Nome: {nome} \nPontos: {pontos}')
    print('1-listar missoes')

    menu=int(input('O que deseja fazer: '))
    match menu:
        case 1:
            for i in range(len(missoes)):
                print(f"\nmissao: {missoes[i]}\n")
        case 2:
            missao=input("Digite a missao que deseja: ")
            missoes.append(missao)
        case 3
