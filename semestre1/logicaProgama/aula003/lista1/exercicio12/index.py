''' 12. Maria quer saber quantos litros de gasolina precisa colocar em seu carro e quanto vai gastar para fazer
uma viagem até a casa de sua irmã.
Dados extras:
- Distância da casa de Maria até sua irmã : 520 km
- Seu carro consome 12 Km/litro de combustível.
- Ela abastece sempre no mesmo posto, onde o preço da gasolina é R$ 4,50 o litro.
Desenvolva um algoritmo onde o usuário digite a distância, o consumo e o valor do litro de
combustível, com estes dados o algoritmo deverá calcular a quantidade de litros de combustível para a
viagem e o custo da viagem.'''

# Exibe mensagem pedindo a distância da viagem em km
print("Digite a distancia que deseja percorrer nessa viajem em km: ")
# Lê a distância informada pelo usuário
distancia = float(input())
# Exibe mensagem pedindo o consumo do veículo (km por litro)
print("Digite quanto o veiculo consome em km/litro: ")
# Lê o consumo informado
consumo = float(input())
# Exibe mensagem pedindo o valor do combustível por litro
print("Digite o valor do combustivel no posto de gasolina que planeja passar: ")
# Lê o valor do combustível
valor = float(input())
# Calcula e exibe a quantidade de litros e o custo total da viagem
print("Com base nos dados fornecido o usuario consumira ", distancia/consumo ," litros de combustivel na viajem e gastara R$ ", (distancia/consumo)*valor ," para comprar o combustivel em toda a viajem")