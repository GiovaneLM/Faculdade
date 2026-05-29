"""
Competências a serem observadas:
- Conhecer os comandos/funções utilizados.
- Saber utilizar os comandos/funções corretamente
- Desenvolver uma solução viável 

Observações:
- Salve o código com o seu nome.
- Dentro do programa, coloque o seu nome como comentário.
- Se fizer o código em alguma plataforma, exporte e envie o arquivo .py
- Você deverá realizar a tarefa individualmente.
- Você pode consultar todos os materiais, só não pode utilizar a IA para realizar código.
- Caso faça perguntas para a IA, coloque os prompts como comentário no final do código. 

"""

'''Item
Enunciado
Implemente um programa em Python que manipule uma lista de números inteiros por meio de um menu interativo. O programa deve permitir ao usuário:
Adicionar número: inserir um novo valor inteiro na lista.
Remover número: excluir um valor específico informado pelo usuário.
Alterar elemento: substituir o valor de um elemento existente por outro.
Localizar elemento: buscar um número na lista e mostrar o índice correspondente.
Consultar por índice: dado um índice, mostrar o elemento armazenado.
Somar elementos: ler dois índices e mostrar a soma dos elementos correspondentes.
O programa deve:
Exibir sempre o conteúdo atual da lista antes de mostrar o menu.
Tratar erros de entrada (ex.: valores não numéricos ou índices inexistentes).'''


'''lista = []

menu = """

    Menu
    ------------------------------------------------
        1- Adicionar um número na lista
        2- Retirar um número da lista
        3- Alterar um elemento da lista
        4- Localizar um elemento e mostrar o seu indice
        5- Ler um indice e mostrar o elemento
        6- ler dois indices e mostrar a soma dos elementos;
    Escolha: """

while True:
    print(lista)
    escolha = input(menu)
    if escolha == "1":
        pass
    if escolha == "2":
        pass
    if escolha == "3":
        pass
    if escolha == "4":
        pass
    if escolha == "5":
        pass
    if escolha == "6":
        pass'''


lista = []
'''ALUNO: GIOVANE LIMEIRA MARTINS'''

while True:
    print('Numeros Atuais na lista')
    print(lista)
    print("Menu")
    print('--------------------------------------------------------------------------------------------------------------------------------------------')
    print('1- Adicionar um número na lista')
    print('2- Retirar um número da lista')
    print('3- Alterar um elemento da lista')
    print('4- Localizar um elemento e mostrar o seu indice')
    print('5- Ler um indice e mostrar o elemento')
    print('6- ler dois indices e mostrar a soma dos elementos;')
    print('0- Sair')
    try:
        escolha = int(input('Escolha:'))
    except:
        print('Opção invalida')
        continue

    if 0 <= escolha <= 6:
        if escolha == 1:
            while True:
                try:
                    numero1=int(input("digite qual o numero que deseja ser adicionado a lista: "))
                    lista.append(numero1)
                    print('\n\n\n')
                    break
                except:
                    print('valor invalido')
                    continue
        elif escolha == 2:
            while True:
                try:
                    numero1=int(input('digite o numero que deseja remover: '))
                except:
                    print('valor invalido')
                    continue
                if numero1 in lista:
                    print(f'numero : {numero1} foi removido com sucesso')
                    lista.remove(numero1)
                    print('\n\n\n')
                    break
                else:
                    print("numero nao encontrado")
                    print('CASO TENHA ESQUECIDO ESSES SAO OS NUMEROS ATUAIS NA LISTA')
                    print(lista)
                    continue
        elif escolha == 3:
                while True:
                    try:
                        numero1=int(input('digite o numero que deseja alterar: '))
                    except:
                        print('valor invalido')
                        continue
                    if numero1 in lista:
                        print(f'numero : {numero1} existe por qual deseja alterar')
                        try:
                            novo=int(input('qual o novo numero que deseja colocar: '))
                        except:
                            print('valor invalido')
                            continue
                        pos=lista.index(numero1)
                        lista[pos]=novo
                        print(f'numero : {numero1} foi subistituido com sucesso por {novo}')
                        print('\n\n\n')
                        break
                    else:
                        print("numero nao encontrado")
                        print('CASO TENHA ESQUECIDO ESSES SAO OS NUMEROS ATUAIS NA LISTA')
                        print(lista)
                        continue
        elif escolha == 4:
            while True:
                try:
                    numero1=int(input('digite o numero que deseja localizar: '))
                except:
                    print('valor invalido')
                    continue
                if numero1 in lista:
                    print(f'numero : {numero1} existe no indice {lista.index(numero1)}')
                    print('\n\n\n')
                    break
                else:
                    print("numero nao encontrado")
                    print('CASO TENHA ESQUECIDO ESSES SAO OS NUMEROS ATUAIS NA LISTA')
                    print(lista)
                    continue
        elif escolha == 5:
            while True:
                try:
                    numero1=int(input('digite a posição do numero que deseja localizar: '))
                except:
                    print('valor invalido')
                    continue
                if 0 <= numero1 <= len(lista):
                    print(f'no indice : {numero1} existe o numero : {lista[numero1]}')
                    print('\n\n\n')
                    break
                else:
                    print("indice invalido")
                    continue
        elif escolha == 6:
            while True:
                try:
                    numero1=int(input('digite a 1° posição do numero que deseja localizar: '))
                except:
                    print('valor invalido')
                    continue
                if 0 <= numero1 <= len(lista):
                    print(f'no indice : {numero1} existe o numero : {lista[numero1]}')
                else:
                    print("indice invalido")
                    continue
                
                try:
                    numero2=int(input('digite a 2° posição do numero que deseja localizar: '))
                except:
                    print('valor invalido')
                    continue
                if 0 <= numero2 <= len(lista):
                    print(f'no indice : {numero2} existe o numero : {lista[numero2]}')
                else:
                    print("indice invalido")
                    continue

                soma = lista[numero1] + lista[numero2]
                print(f'a soma dos valores e igual a: {soma}')
                print('\n\n\n')
                break
        else :
            print("Obrigado por usar meu software Adeus")
            print("Aluno : Giovane Limeira Martins ")
            break
    else:
        print("Opção invalida")
        continue

