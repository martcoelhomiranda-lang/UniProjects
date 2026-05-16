# Escrever um algoritmo que leia um número não determinado de valores e calcule a
# média aritmética dos valores lidos, a quantidade de valores positivos, a quantidade
# de valores negativos e o percentual de valores negativos e positivos. Mostre os
# resultados.

positivos = 0
negativos = 0
soma_p = 0
soma_n = 0
continuar = True
while continuar:
    n = int(input("Digite um numero: "))
    if n > 0:
        positivos += 1
        soma_p += n
    else:
        if n < 0:
            negativos += 1
            soma_n += n
    reposta = input("Deseja continuar? [S/N] ")
    if reposta == "n":
        continuar = False
print(f"Quantidade de numeros positivos:{positivos}")
print(f"Quantidade de numeros negativos:{negativos}")
print(f"Soma de positivos: {soma_p}")
print(f"Soma de negativos: {soma_n}")
total = positivos + negativos
if total != 0:
    print(f"Porcentagem de numeros positivos:{(positivos/total)*100}%")
    print(f"Porcentagem de numeros negativos:{(negativos/total)*100}%")
    print(f"A media aritmetica é:{soma_p + soma_n/ total}")

