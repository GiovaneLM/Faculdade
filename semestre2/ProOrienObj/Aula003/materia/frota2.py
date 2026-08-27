class Veiculo():
    #self define os atributos do objeto
    #metodo __init__ = metodo construção
    def __init__(self,marca,modelo,ano,motor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.motor = motor
        self.velocidade = 0
    #metodo listar
    def listar(self):
        print(f'\nMarca {self.marca}')
        print(f'Modelo {self.modelo}')
        print(f'Ano {self.ano}')
        print(f'Motorização {self.motor}')
        print(f'Velocidade {self.velocidade} Km/h {'em Movimento 'if self.velocidade >0 else 'Parado'}')
    #metodo acelerar
    def acelerar(self):
        if self.velocidade >= 150:
            print('Alcançou Limite Máximo {self.velocidade}')
        else:
            self.velocidade +=10
    #metodo acelerar
    def frear(self):
        self.velocidade-=10

    def trocarMotor(self):
        motorNovo = input('nova motorização: ')
        self.motor = motorNovo



#função do programa (FORA DA CLASS)
def entrada_de_dados():
    marca = input('Marca: ')
    modelo = input('modelo: ')
    ano = int(input('ano: '))
    motor= input('motorização: ')
    return marca,modelo,ano,motor



#inicio programa
#chama função do programa para entrar conteudo
marca,modelo,ano,motor=entrada_de_dados()
#usando metodo com nome da class usa __init__
#cria objeto
fusca = Veiculo(marca,modelo,ano,motor)
fusca.listar()

for i in range(10):
    fusca.acelerar()
fusca.listar()

for i in range(10):
    fusca.frear()
fusca.listar()

fusca.trocarMotor()
fusca.listar()