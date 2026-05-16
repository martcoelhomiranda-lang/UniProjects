# Escrever um algoritmo que leia uma variável n e calcule a tabuada de 1 até n.
# Mostre a tabuada na forma:
# 1 x n = n
# 2 x n = 2n
# 3 x n = 3n
# ...............
# n x n = n2

n = int(input("Quer a tabuada de que numero?: "))
if n <= 0:
    print("Valor invalido")
else:
    z = 0
    y = 0
    
    for conta in range(n):
        z += 1
        resultado = n * z
        print( n, "x", z, "=", resultado)


