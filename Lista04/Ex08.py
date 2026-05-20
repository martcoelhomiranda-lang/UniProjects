# Escreva uma função que receba como parâmetro um
# valor n inteiro e positivo e que calcule a seguinte
# soma: S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n . A função
# deverá retornar o valor de S

def calcularSoma(n):
    for i in range(1, n):
        s = 1 + n/i
        return s

n = int(input("Digite um valor: "))
print(calcularSoma(n))