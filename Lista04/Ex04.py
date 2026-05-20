# Escrever uma função contarImpar(n1, n2) que retorna
# o número de inteiros ímpares que existem entre n1 e
# n2 (inclusive ambos, se for o caso). A função deve
# funcionar inclusive se o valor de n2 for menor que n1.

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

def contarImpar(n1, n2):
    impares = 0
    troca = 0

    if n1 > n2:
        troca = n1
        n1 = n2
        n2 = troca

    for i in range(n1 , n2 + 1):
        if i % 2 == 1:
            impares += 1
    return impares

print(contarImpar(n1, n2))









