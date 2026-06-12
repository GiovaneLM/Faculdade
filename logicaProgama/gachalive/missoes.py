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

def validar(nome, Missoes_nConcluidas):
    if nome in Missoes_nConcluidas:
        return True
    print('missao nao encontrada\n')
    return False 