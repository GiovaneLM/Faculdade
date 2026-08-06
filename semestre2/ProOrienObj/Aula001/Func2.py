#Função sem parametro e sem retorno
def alo(nome):
    print(f'Ola,{nome}')
    print('Bem Vindo a POO!')
    if nome=='GABRIEL':
        print('Você é LINDÃO')


while True:
    nomeAluno=input('Digite um nome: ').upper()
    if nomeAluno=="FIM":
        print('Adeus👍')
        break
    alo(nomeAluno)