class Veiculo:
    marca = ''
    modelo = ''
    ano = 0
    motor = ''
    velocidade = 0

    def listar(self):
        print(f'\nMarca {self.marca}')
        print(f'Modelo {self.modelo}')
        print(f'Ano {self.ano}')
        print(f'Motorização {self.motor}')
        print(f'Velocidade {self.velocidade} Km/h {'em Movimento 'if self.velocidade >0 else 'Parado'}')

    def acelerar(self):
        if self.velocidade >= 150:
            print('Alcançou Limite Máximo {self.velocidade}')
        else:
            self.velocidade +=10

    def frear(self):
        self.velocidade-=10






fusca = Veiculo()
fusca.marca = 'Volkswagen'
fusca.modelo = '2 portas'
fusca.ano = 1970
fusca.motor = 'Gasolina 1300'
fusca.velocidade = 0
fusca.listar()

fusca.velocidade += 10
fusca.listar()

print('Acelerar')
for i in range(10):
    fusca.acelerar()
fusca.listar()

print('frear')
for i in range(11):
    fusca.frear()

fusca.listar()