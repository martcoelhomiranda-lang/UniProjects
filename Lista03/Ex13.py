#  Faça um algoritmo que leia uma quantidade não determinada de números positivos.
# Calcule a quantidade de números pares e ímpares, a média de valores pares e a
# média geral dos números lidos. O número que encerrará a leitura será zero.

n = int(input("Digite um numero inteiro e positivo (zero para encerrar): "))
pares = 0
impares = 0
soma = 0
soma_geral = 0
geral = 0

while n > 0:
    if n % 2 == 0:
        pares += 1
        soma += n
    else:
        if n % 2 != 0:
            impares += 1
            soma_geral = soma + impares
    geral = impares + pares
    n = int(input("Digite um numero inteiro e positivo (zero para encerrar): "))

print(f"A quantidade de pares é: {pares}")
print(f"A quantidade de impares é: {impares}")
print(f"A media de valores pares é: {soma/pares}")
print(f"A media dos valores gerais é: {soma_geral/geral}")

