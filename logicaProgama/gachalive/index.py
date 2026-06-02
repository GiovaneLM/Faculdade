import random
missoes=[]
recompensas=[]
nome=""
pontos=1500
nome=input("ola usuario nos informe seu nome: ")

while True:
    for i in range(30):
        print("-",end="")
    print(f'\nNome: {nome} \nPontos: {pontos}')
    print('1-listar missoes')
    print('2-adicionar missao')
    print('3-deletar missao')
    print('4-concluir missao')
    print('5-listar recompensa')
    print('6-adicionar recompensa')
    print('7-deletar recompensa')
    print('8-resgatar recompensa')
    print('9-editar perfil')
    print('0-SAIR')


    menu=int(input('O que deseja fazer: '))
    match menu:
        case 1:
            for i in range(len(missoes)):
                print(f"\nmissao: {missoes[i]}\n")
        case 2:
            missao=input("Digite a missao que deseja: ")
            missoes.append(missao)
            print("missao adicionada com sucesso\n")
        case 3:
            missao=input('digite a missao que deseja deletar: ')
            if missao in missoes:
                missoes.remove(missao)
                print('missao removida com sucesso\n')
            else:
                print('missao nao encontrada\n')
        case 4:
            missao=input('digite a missao que deseja concluir: ')
            if missao in missoes:
                missoes.remove(missao)
                print('missao concluida com sucesso\n')
                pontos += 100
            else:
                print('missao nao encontrada\n')
        case 5:
            for i in range(len(recompensas)):
                print(f"\nrecompensa: {recompensas[i][0]}\ndescrição: {recompensas[i][1]}")
        case 6:
            recompensa=input("Digite a recompensa que deseja: ")
            descricao=input("digite a descriçao dessa recompensa: ")
            if descricao == " ":
                descricao = 'vazio'
            recompensas.append([recompensa,descricao])
            print("recompensa adicionada com sucesso\n")
        case 7:
            recompensa=input('digite a recompensa que deseja deletar: ')
            if recompensa in recompensas:
                recompensas.remove(recompensa)
                print('recompensa removida com sucesso\n')
            else:
                print('recompensa nao encontrada\n')
        case 8:
            if pontos >= 500:
                print("voce tem pontos o suficiente para resgatar uma recompensa")
                resposta=input("deseja fazer isso S-sim/N-não: ").lower()
                if resposta == "sim" or resposta == "s":
                    numero = random.randrange(len(recompensas))
                    print(f"\nrecompensa: {recompensas[numero][0]}\ndescrição: {recompensas[numero][1]}")
                    pontos -= 500
                else:
                    print("ok!!!!!")
            else:
                print("voce NÃO tem pontos o suficiente para resgatar uma recompensa")
        case 9:
            nome=input("Digite o novo nome que deseja usar: ")
            print(f"nome alterado para {nome} com sucesso!!!!")
        case 0:
            print("Obrigado por usar meu software")
            break