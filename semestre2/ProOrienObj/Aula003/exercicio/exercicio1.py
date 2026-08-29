# e roupas. O sistema deve permitir o cadastro de novas peças, a visualização dos dados e 
# o registro de vendas com baixa no estoque. 
# Requisitos: 
# 1.  Crie a classe Camisa. 
# 2.  No método construtor __init__, defina e inicialize os seguintes atributos: 
# ○  cor (texto) 
# ○  tamanho (texto: "P", "M", "G", "GG") 
# ○  preco (número decimal) 
# ○  tipo_gola (texto: ex: "Gola Polo", "Gola V", "Gola Redonda") 
# ○  quantidade_estoque (número inteiro) 
# 3.  Implemente os seguintes métodos na classe: 
# ○  exibir_informacoes(): Mostra na tela todos os dados da camisa de forma organizada. 
# ○  vender(quantidade):  Recebe  a  quantidade  de  peças  a  serem  vendidas.  Se  houver 
# estoque suficiente, realiza a subtração e exibe o estoque restante; caso contrário, exibe 
# uma mensagem avisando que o estoque é insuficiente. 
# 4.  Área de Teste: 
# ○  Crie um objeto da classe Camisa (ex: cor "Azul", tamanho "M", preço 79.90, gola "Polo", 
# estoque 10). 
# ○  Chame o método exibir_informacoes(). 
# ○  Realize uma venda válida (ex: 3 unidades). 
# ○  Tente realizar uma venda com quantidade maior do que o estoque disponível para testar 
# a validação. 
# Conteúdo gerado com suporte de Inteligência Artificial para estruturação pedagógica e adaptado, revisado e validado tecnicamente pelo Professor.  

class Camisa():
    def __init__(self,cor,tamanho,preco,tipo_gola,quantidade_estoque):
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco
        self.tipo_gola = tipo_gola
        self.quantidade_estoque = quantidade_estoque

    def exibir_informacoes(self):
        print(f'\nCor: {self.cor}')
        print(f'Tamanho: {self.tamanho}')
        print(f'Preço: {self.preco}')
        print(f'Tipo de Gola: {self.tipo_gola}')
        print(f'Quantidade no Estoque: {self.quantidade_estoque}')

    def venda(self):
        while True:
            try:
                quantidade_venda = int(input('quantidade a ser vendida de camisas: '))
                break
            except:
                print('digite algo valido')
        if quantidade_venda <= self.quantidade_estoque:
            self.quantidade_estoque -= quantidade_venda
        else:
            print('a quantidade que esta tentando vender nao bate com a quantidade em estoque')


def entrada_de_dados():
    cor = input('Cor: ')
    while True:
        tamanho = input('Tamanho: \"P\", \"M\",\"G\",\"GG\":').upper()
        if tamanho == 'P' or tamanho == 'M' or tamanho == 'G' or tamanho == 'GG':
            break
        else:
            print('tamanho invalido')
    while True:
        try:
            preco = float(input('Preço: '))
            break
        except:
            print('digite um valor valido')
    tipo_gola = input('texto: ex: "Gola Polo", "Gola V", "Gola Redonda: ')
    while True:
        try:
            quantidade_estoque = int(input('Qunatidade no estoque: '))
            break
        except:
            print('digite um valor valido')
    return cor,tamanho,preco,tipo_gola,quantidade_estoque



cor,tamanho,preco,tipo_gola,quantidade_estoque=entrada_de_dados()

renner = Camisa(cor,tamanho,preco,tipo_gola,quantidade_estoque)
renner.exibir_informacoes()
renner.venda()
renner.exibir_informacoes()