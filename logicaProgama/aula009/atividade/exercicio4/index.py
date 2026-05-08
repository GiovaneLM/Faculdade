# Exercício 1:
# Faça um algoritmo que leia uma quantidade indeterminada de números (finalize quando digitado a palavra 'fim')
# No final diga:
# quantos números negativos foram digitados,
# quantos números pares,
# quantos números digitados estão no intervalo de 10 e 30, ou no intervalo de 50 e 70.


negativos=0
pares=0
intervalos=0
lst_negativo=[]

while True:
    entrada = input("digite um numero ou fim: ")

    if entrada.lower()=="fim":
        break

    try:
        numero=int(entrada)

        if numero<0:
            negativos+=1
            lst_negativo.append(numero)
        if numero%2 == 0:
            pares+=1
        if(10<=numero and numero<=30) or (50<=numero and numero<=70):
            intervalos+=1
    
    except ValueError:
        print("entrada invalida")

print("RESULTADO")
print(f"numeros negativos {len(lst_negativo)} - {lst_negativo}")
print(f"numeros pares {pares}")
print(f"numeros intervalo {intervalos}")