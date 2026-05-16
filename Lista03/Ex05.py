# Chico tem 1,50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1,30 metro
# e cresce 3 centímetros por ano. Construa um algoritmo que calcule e imprima
# quantos anos serão necessários para que Zé seja maior que Chico.

chico = 150
ze = 130
resultado = 0

for anos in range(1, 200):
    chico += 2
    ze += 3
    if ze > chico and resultado == 0:
        resultado = anos

print(f"Sao necessarios {resultado} anos para que ze fique maior que chico")
