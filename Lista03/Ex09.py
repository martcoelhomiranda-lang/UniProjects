#  Escrever o algoritmo que leia os valores n1 e n2 e imprima o intervalo fechado
# (incluindo os limites) entre esses dois valores.

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

if n1 > n2:
    aux = n1
    n1 = n2
    n2 = aux
    for i in range(n1,n2 +1):
        print(i)
