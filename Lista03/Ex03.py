# Faça um algoritmo que lê um valor N inteiro e positivo e que calcula e escreve o
# fatorial de N (N!).

n = int(input("DIgite um valor inteiro e positivo: "))
res = 1
e = 1
for i in range(1,n+1):
    res *= i
    e += 1/res

print(e)