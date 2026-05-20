# Escrever uma função somarIntervalo(n1, n2) que
# retorna a soma dos números inteiros que existem
# entre n1 e n2 (inclusive ambos). A função deve
# funcionar inclusive se o valor de n2 for menor que n1

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

if n1 == n2:
    soma1 = n1 + n2
    print(soma1)
else:
    def somarintervalo(n1, n2):

        soma = 0

        for i in range(n1, n2 + 1):
            if n1 > n2:
                troca = n1
                n1 = n2
                n2 = troca
            else:
                soma += i
        return soma

print(somarintervalo(n1, n2))

