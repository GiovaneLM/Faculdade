def Desconto10(valor):
    return (valor * 0.9)

def Desconto20(valor):
    return (valor * 0.8)

def calcular_desconto(valor,cupom):
    if cupom=='DESCONTO10':
        return Desconto10(valor)
    elif cupom=='DESCONTO20':
        return Desconto20(valor)
    else:
        return (valor)

valor_compra = 0
cupom="nenhum"
while True:
    for i in range(50):
        print('#', end='')
    print('\nBem Vindo ao ByteShop')
    print(f'carrinho: R${valor_compra}')
    if cupom == 'DESCONTO10' or cupom == 'DESCONTO20':
        print('cupom ativado')
    while True:
        try:
            menu= int(input('1-adicionar carrinho \n2-ativar cupom \n3-fechar carrinho \ndigite o que deseja fazer: '))
            break
        except:
            print('digite um numero valido')
    if menu == 1:
        while True:
            try:
                valor_produto=float(input('digite o valor do produto: R$'))
                break
            except:
                print('digite algo valido')
        valor_compra += valor_produto
    elif menu == 2:
        cupom=input('digite um cupom valido: ').upper()
        if cupom == 'DESCONTO10' or cupom == 'DESCONTO20':
            print('cupom ativado')
    elif menu == 3:
        print('calculando descontos')
        valor_final=calcular_desconto(valor_compra,cupom)
        print(f'valor final da compra : R$ {valor_final}')
        print('obrigado por comprar conosco')
        valor_compra = 0
        cupom = "nenhum"
    else:
        print('opção invalida')
