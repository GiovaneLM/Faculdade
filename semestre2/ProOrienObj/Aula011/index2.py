class Veiculo:
    def __init__(self,marca,modelo,ano,preco_diaria):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco_diaria = preco_diaria

    def calcular_aluguel(self,dias):
        print(f'valor do aluguel para {dias} é {dias * self.preco_diaria}')

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, preco_diaria,numero_portas):
        super().__init__(marca, modelo, ano, preco_diaria)
        self.numero_portas = numero_portas

    def calcular_aluguel(self, dias):
        if dias > 7 :
            valor_aluguel = (dias * self.preco_diaria) - (dias * self.preco_diaria) * 0.10
        else:
            valor_aluguel = (dias * self.preco_diaria)
        print(f'valor do aluguel {self.modelo} para {dias} é {valor_aluguel}')

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, preco_diaria,cilindrada):
        super().__init__(marca, modelo, ano, preco_diaria)
        self.cilindrada = cilindrada

    def calcular_aluguel(self, dias):
        valor_aluguel = (dias * self.preco_diaria) + (dias * self.preco_diaria) * 0.05
        print(f'valor do aluguel {self.modelo} para {dias} é {valor_aluguel}')

moby = Carro('Fiat','Moby xyz',2026,250,4)
moto1 = Moto('Honda','CG Titanium',2025,155.75,160)

moby.calcular_aluguel(4)
moto1.calcular_aluguel(10)

moby.calcular_aluguel(8)