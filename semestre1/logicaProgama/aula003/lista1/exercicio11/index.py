'''Escrever um algoritmo para ler uma temperatura em Fahrenheit e apresentá-la convertida em graus
Centígrados.
                        (Fahrenheit – 32) x 5
Fórmula: Centígrados = ----------------------------
                                    9'''

# Exibe mensagem pedindo a temperatura em Fahrenheit
print("digite a temperatura atual em Fahrenheit para ser convertido : ")
# Lê o valor digitado e armazena na variável Fah
Fah = float(input())
# Calcula e exibe a temperatura convertida para Celsius
print("Resultado : ", ((Fah - 32)*5)/9,"°C")