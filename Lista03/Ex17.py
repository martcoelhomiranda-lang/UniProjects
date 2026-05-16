# Escrever um algoritmo que lê 10 valores, um de cada vez, e conte quantos deles
# estão no intervalo [10,20] e quantos deles estão fora do intervalo, escrevendo estas
# informações.

dentro = 0
fora = 0

for i in range(10):
    n = int(input("Digite um valor: "))
    if n >= 10 and n <= 20:
        dentro += 1
    else:
        fora += 1
print(f"Existem {dentro} valores dentro do intervalo [10,20]")
print(f"Existem {fora} valores fora do intervalo [10,20]")
