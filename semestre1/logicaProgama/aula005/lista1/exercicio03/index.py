'''Exercício 03.
Faça um algoritmo que leia uma frase digitada pelo usuário e imprima essa frase na tela. 
Imprima também a quantidade de caracteres digitados e q quantidades de letras ' a ' existentes.'''
# Lê uma frase digitada pelo usuário e armazena na variável frase
frase = input("Digite uma frase: ")

# Exibe a frase digitada, pulando uma linha antes dela
print("Frase digitada: \n" , frase)

# Exibe a quantidade de caracteres da frase usando a função len()
print(f"quantidade de caracteres =  {len(frase)}")

# Cria uma variável contador para contar quantas letras 'a' existem na frase
qt_a = 0

# Percorre cada caractere da frase
for caracter in frase:

    # Verifica se o caractere atual é igual a 'a'
    if caracter =='a':

        # Soma 1 ao contador de letras 'a'
        qt_a = qt_a + 1 #qt_a += 1

# Exibe a quantidade de letras 'a' encontradas
print(f"quantdade de a = {qt_a}")

# Reinicia o contador de letras 'a'
qt_a = 0

# Percorre os índices da frase de 0 até o último caractere
for i in range(len(frase)):

    # Verifica se o caractere naquela posição é igual a 'a'
    if frase[i] =='a':

        # Soma 1 ao contador
        qt_a += 1

# Exibe novamente a quantidade de letras 'a'
print(f"quantdade de a = {qt_a}")

# Usa o método count para contar diretamente quantas letras 'a' existem na frase
qt_a = frase.count('a')

# Exibe a quantidade de letras 'a' encontrada com count()
print(f"quantdade de a = {qt_a}")

# Exibe a frase usando chaves, mas aqui será mostrado um conjunto por causa das {}
print("Frase digitada: " , {frase})

# Exibe a frase usando o método format()
print("Frase digitada: {}" .format(frase))



# Armazena o texto "Frase Digitada" na variável x
x = "Frase Digitada"

# Exibe o conteúdo inteiro da variável x
print(x)

# Armazena novamente o texto "Frase Digitada" na variável x
x = "Frase Digitada"

# Exibe o caractere da posição 2 da string
print(x[2])

# Armazena novamente o texto "Frase Digitada" na variável x
x = "Frase Digitada"

# Exibe os caracteres da posição 2 até a posição 6
print(x[2:7])

# Armazena novamente o texto "Frase Digitada" na variável x
x = "Frase Digitada"

# Cria a variável y com os caracteres da posição 0 até a 4
y = x[0:5]

# Exibe o conteúdo de y
print(y)

# Exibe novamente os caracteres da posição 2 até a 6
print(x[2:7])


# Armazena novamente o texto "Frase Digitada" na variável x
x = "Frase Digitada"

# Percorre todas as posições da string x
for posicao in range(len(x)):

    # Exibe a posição e o caractere correspondente
    print(posicao , x[posicao])

# Substitui todas as letras 'a' por 'A' na string e salva o resultado em x
x = "Frase Digitada".replace('a' , 'A')

# Exibe a nova string com as substituições
print(x)

# Converte a string em uma lista de caracteres
x=list("frase digitada")

# Altera o primeiro caractere da lista para "P"
x[0] = "P"

# Exibe a lista modificada
print(x)


# Inicia um laço infinito
while True:

    # Lê algo digitado pelo usuário
    x = input("digite algo: ")

    # Verifica se o que foi digitado contém apenas números
    if x.isnumeric():

        # Exibe mensagem informando que é um número
        print("isto é um numero: ")

        # Encerra o laço
        break

    # Caso não seja número
    else:

        # Exibe mensagem informando que não é número
        print("nao e numero:")