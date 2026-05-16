# Escrever um algoritmo que leia uma quantidade desconhecida de números e conte
# quantos deles estão nos seguintes intervalos: [0,25], [26,50], [51,75] e [76,100]. A
# entrada de dados deve terminar quando for lido um número negativo.

n = int(input("Digite um numero (negativo para encerrar): "))
intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0
while n >= 0:
    if n >= 0 and n <= 25:
        intervalo1 += 1
    else:
        if n >= 26 and n <= 50:
            intervalo2 += 1
        else:
            if n >= 51 and n <= 75:
                intervalo3 += 1
            else:
                if n >= 76 and n <= 100:
                    intervalo4 += 1
    n = int(input("Digite um numero (negativo para encerrar): "))

print(f"De 0 a 25 existem {intervalo1} numeros")
print(f"De 26  a 50 existem {intervalo2} numeros")
print(f"De 51 a 75 existem {intervalo3}  numeros")
print(f"De 76 a 100 existem {intervalo4} numeros")
