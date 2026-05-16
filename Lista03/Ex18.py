# Escrever um algoritmo que gere e escreva os 3 primeiros números perfeitos. Um
# número perfeito é aquele que é igual a soma dos seus divisores. (Ex.: 6 = 1+2+3;
# 28= 1+2+4+7+14, etc).

perfeitos = 0
n = 1

while perfeitos < 3:
    n += 1
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    if soma == n:
        print(n)
        perfeitos += 1