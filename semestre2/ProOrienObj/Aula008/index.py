class Caminhao:
    def __init__(self,modelo,placa,capacidade_carga):
        self.modelo = modelo
        self.placa = placa
        self.capacidade_carga = capacidade_carga
        self.capacidade_disponivel = capacidade_carga
    def carregar(self,peso):
        if peso < 0:
            print('digite um peso valido')
        elif peso <= self.capacidade_carga and peso <= self.capacidade_disponivel:
            self.capacidade_disponivel = self.capacidade_disponivel - peso
            print(f'valorcapacidade maxima :{self.capacidade_carga} capacidade atual disponivel: {self.capacidade_disponivel}')
        else:
            print('valor invalido por passor da capacidade maxima')

    def descarregar(self,peso):
        if peso < 0:
            print('valor invalido')
        elif peso <= self.capacidade_disponivel:
            self.capacidade_disponivel = self.capacidade_disponivel + peso
            print(f'valor valido capacidade maxima :{self.capacidade_carga} capacidade atual disponivel: {self.capacidade_disponivel}')
        else:
            print('valor nao aceito')
class Motorista:
    def __init__(self,nome,idade,cnh,datavalidade):
        self.nome = nome
        self.idade = idade
        self.cnh = cnh
        self.datavalidade = datavalidade

