#Exercício 04.
#Faça um algoritmo que leia o nome e a idade de uma pessoa e imprima a mensagem :
#- "Você é jovem" se a pessoa tiver menos de 18 anos.
#- "Você é um adulto" Se a pessoa tiver a idade entre 18 e 60 anos.
#- "Você é um idoso" Se a pessoa tiver mais que 60 anos.

print("digite sua idade ")
idade = int(input())

if idade < 18:
    print("Você é jovem")
elif 18 <= idade and idade <= 60:
    print("Você é um adulto")
else:
    print("Você é um idoso")