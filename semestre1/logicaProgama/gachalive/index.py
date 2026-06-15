import random
###################################################################################################################
#FUNÇOES DE MISSAO
def Listar_Missoes(Missoes_nConcluidas):
    for i in range(len(Missoes_nConcluidas)):
        print(f"\n{i+1}° missao: {Missoes_nConcluidas[i]}\n")

def Criar_Missoes():
    nome=input("Digite a missao que deseja: ")
    print("missao adicionada com sucesso\n")
    return nome

def Deletar_Missoes(Missoes_nConcluidas):
    nome=input('digite a missao que deseja deletar: ')
    if nome in Missoes_nConcluidas:
            Missoes_nConcluidas.remove(nome)
            print('missao removida com sucesso\n')
    else:
        print('missao nao encontrada\n')

def Concluir_Missoes(pontos, Missoes_nConcluidas, Missoes_Concluidas):
    nome=input('digite a missao que deseja concluir: ')
    if nome in Missoes_nConcluidas:
        if nome not in Missoes_Concluidas:
            Missoes_Concluidas.append(nome)
            print('missao concluida com sucesso\n')
            pontos += 100
        else:
            print('essa missao ja foi concluida')
    else:
        print('missao nao encontrada\n')
    return pontos

def validarM(nome, Missoes_nConcluidas):
    if nome in Missoes_nConcluidas:
        return True
    print('missao nao encontrada\n')
    return False 




Missoes_nConcluidas=["Teste"]
Missoes_Concluidas=[]
recompensas=[]
nome=""
pontos=1500
nome=input("ola usuario nos informe seu nome: ")

while True:
    print(Missoes_Concluidas)
    for i in range(30):
        print("-",end="")
    print('\n')
    if len(Missoes_nConcluidas) > 1:
        print('algumas missoes ja registradas')
        for i in range(2):
            print(f'{i+1}° missao : {Missoes_nConcluidas[i]}')
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
            Listar_Missoes(Missoes_nConcluidas)
        case 2:
            Missoes_nConcluidas.append(Criar_Missoes())
        case 3:
            Deletar_Missoes(Missoes_nConcluidas)
        case 4:
            pontos = Concluir_Missoes(pontos,Missoes_nConcluidas, Missoes_Concluidas)
        case 5:
            for i in range(len(recompensas)):
                print(f"\nrecompensa: {recompensas[i]}\n")
        case 6:
            recompensa=input("Digite a recompensa que deseja: ")
            recompensas.append(recompensa)
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
                    print(f"\nrecompensa: {recompensas[numero]}\n")
                    pontos -= 500
                elif resposta == 'nao' or resposta == 'não' or resposta == 'n':
                    print('ok')
                else:
                    print("TU É LESO?")
            else:
                print("voce NÃO tem pontos o suficiente para resgatar uma recompensa")
        case 9:
            nome=input("Digite o novo nome que deseja usar: ")
            print(f"nome alterado para {nome} com sucesso!!!!")
        case 0:
            print("Obrigado por usar meu software")
            break