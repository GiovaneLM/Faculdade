lista = []

############################################################################
# FUNÇÕES DE VALIDAÇÃO
def numero_valido(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except:
            print("OPS. ")

def validar_numero(numero):
    if numero in lista:
        return True, numero  # número está na lista
    return False, numero     # número não está na lista

def validar_index(numero):
    if 0 <= numero <= len(lista):
        return True,numero
    return False,numero


############################################################################
# FUNÇÕES DE PRINCIPAIS
def adicionar():
    lista.append(numero_valido("Digite um Número: "))

def remover():
    numero_ok, numero_correto = validar_numero(numero_valido("Número a ser removido: "))
    if numero_ok:
        lista.remove(numero_correto)
    else:
        print("Número não está na lista.")

def alterar():
    numero_ok,numero = validar_numero(numero_valido("Número a ser alterado: "))
    if numero_ok:
        pos=lista.index(numero)
        novo=numero_valido("Qual o novo Número que deseja colocar: ")
        lista[pos]=novo
    else:
        print("Número não está na lista.")

def posicao_num():
    numero_ok,numero_correto=validar_numero(numero_valido("Número a ser localizado: "))
    if numero_ok:
        pos=lista.index(numero_correto)
        print(f"Número esta na posição {pos}")
    else:
        print("Número não está na lista.")

def posicao_index():
    numero_ok,numero_correto=validar_index(numero_valido("Posição a ser localizado: "))
    if numero_ok:
        print(f"Número na posição ,é: {lista[numero_correto]}")
    else:
        print("Posição não está na lista.")

def numero():
    numero_ok,numero_correto=validar_index(numero_valido("posição a ser localizado: "))
    if numero_ok:
        return numero_correto
    else:
        print("Número não está na lista.")

def matematica():
    num1=numero()
    num2=numero()
    print(f"a soma dos numeros nas posições fornecidas {num1 + num2}")

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

############################################################################
# Programa Principal
while True:
    print(lista)

    escolha =numero_valido(menu)

    if escolha == 1:
        adicionar()
    elif escolha == 2:
        remover()
    elif escolha == 3:
        alterar()
    elif escolha == 4:
        posicao_num()
    elif escolha == 5:
        posicao_index()
    elif escolha == 6:
        matematica()
    else:
        print('Opção invalida')
