# função sem parâmetro com Retorno de valor
def soma():
    while True:
        try:
            n1=int(input('Digite um valor: '))
            n2=int(input('Digite um valor: '))
            break
        except:
            print("Criatura digite valores INTEIROS")
    return (n1+n2)

#Inicio Programa
for i in range(5):
    print(f'A soma é {soma()}')