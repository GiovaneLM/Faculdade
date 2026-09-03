class Produto():
    def __init__(self,codigoProduto,nomeProduto,preco,quantidadeEstoque ):
        self.codigoProduto = codigoProduto
        self.nomeProduto = nomeProduto
        self.preco = preco
        self.quantidadeEstoque = quantidadeEstoque

    def exibirDetalhes(self):
        print(f"ID: [{self.codigoProduto}] | Produto: [{self.nomeProduto}] | Preço: R$ [{self.preco}] | Estoque: [{self.quantidadeEstoque}]")

    def atualizarPreco(self):
        novo_preco = float(input('digite o novo preço: '))
        self.preco = novo_preco

    def vender(self):
        while True:
            try:
                quantidade = int(input('Digite a quantidade a ser vendida: '))
                if quantidade <= 0:
                    print('A quantidade deve ser maior que zero.')
                    continue
                if quantidade <= self.quantidadeEstoque:
                    self.quantidadeEstoque -= quantidade
                    print(f'Venda realizada! \nQuantidade atual do estoque: {self.quantidadeEstoque}')
                    break
                else:
                    print(
                        f'Estoque insuficiente! \nQuantidade disponível: {self.quantidadeEstoque}')
            except ValueError:
                print('Digite uma quantidade válida.')


def validar(tipo):
    while True:
        try:
            if tipo == 'codigoProduto':
                return int(input('Digite o numero do codigo do Produto: '))
            elif tipo == 'nomeProduto':
                return input('digite o nome do produto: ')
            elif tipo == 'preco':
                return float(input('digite o preço do produto: '))
            elif tipo == 'quantidadeEstoque':
                return int(input('Digite o numero no Estoque: '))
            else:
                print('Tipo inválido.')
                return None
        except ValueError:
            print('Digite um valor válido.')


def entrada_de_dados():
    codigoProduto = validar('codigoProduto')
    nomeProduto = validar('nomeProduto')
    preco = validar('preco')
    quantidadeEstoque = validar('quantidadeEstoque')
    return codigoProduto,nomeProduto,preco,quantidadeEstoque


codigoProduto,nomeProduto,preco,quantidadeEstoque= entrada_de_dados()
produto = Produto(codigoProduto,nomeProduto,preco,quantidadeEstoque)
produto.exibirDetalhes()
produto.atualizarPreco()
produto.exibirDetalhes()
produto.vender()
produto.exibirDetalhes()