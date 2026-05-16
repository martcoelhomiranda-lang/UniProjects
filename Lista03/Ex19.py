# Escrever um algoritmo que leia um valor N inteiro e positivo e que calcula o valor
# de E. Imprime o resultado de E ao final.
# E = 1 + 1 / 1! + 1 / 2! + 1 / 3! + 1 / N!

n = int(input("DIgite um valor inteiro e positivo: "))
res = 1
e = 1
for i in range(1,n+1):
    res *= i
    e += 1/res

print(e)