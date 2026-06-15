'''10. Fazer um algoritmo para ler duas notas, os pesos de cada nota e mostrar a média ponderada.
                                (nota 1 * peso da nota 1) + (nota 2 * peso da nota 2)
Cálculo da Média Ponderada = ------------------------------------------------------------------------
                                                        soma dos pesos'''

# Exibe mensagem pedindo a primeira nota
print("digite o valor da sua 1° nota da  materia : ")
# Lê o valor da primeira nota
nota1 = float(input())
# Exibe mensagem pedindo o peso da primeira nota
print("digite o valor do peso dessa  nota : ")
# Lê o peso da primeira nota
peso1 = float(input())
# Exibe mensagem pedindo a segunda nota
print("digite o valor da sua 2° nota da  materia : ")
# Lê o valor da segunda nota
nota2 = float(input())
# Exibe mensagem pedindo o peso da segunda nota
print("digite o valor do peso dessa  nota : ")
# Lê o peso da segunda nota
peso2 = float(input())
# Exibe explicação da fórmula da média ponderada
print("o calculo da sua media das notas é : ((nota 1 x peso da nota)+(nota 2 * peso da nota 2 )) / soma dos pesos")
# Mostra como o cálculo será feito com os valores informados
print("nesse caso o calculo sera : ((", nota1 ," x " , peso1,") + (", nota2 , " x ", peso2,") ) / (",peso1,"+",peso2,")" )
# Calcula e exibe o resultado da média ponderada
print("resultado : ", ((nota1*peso1)+(nota2*peso2))/(peso1+peso2))